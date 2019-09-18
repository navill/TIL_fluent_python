import argparse
import collections
import pprint
import queue
import random
import time

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')


class Simulator:
    # taxi = {0: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL), 1: ...,}
    # Simulator(taxi)
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()

        # procs_map이 아닌 dict(procs_map)인 이유
        # 사본을 만들어 self.procs에 저장함으로써 호출자가 전달한 dict 객체와 분리된다.
        # -> self.procs는 호출자가 전달한 dict 객체에 영향을 미치지 않는다.
        # -> StopIteration 발생 시 해당 self.procs 객체는 del 구문에 의해 삭제된다.
        # -> 하지만 호출자가 전달한 객체는 삭제되지 않는다(운행을 중단한다고 해서 현실 세계의 택시가
        # 사라지면 안됨).
        self.procs = dict(procs_map)
        self.temp_list = []

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            # priming - texi_process의 첫 번째 yield
            first_event = next(proc)
            # first_event = 기동된 coroutine 객체 -> 0, 1, 2 순으로 queue에 삽입
            self.events.put(first_event)
        i = 0
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            self.temp_list.append({i: current_event})
            i += 1
            # current_event = PriorityQueue에 들어간 Event 객체
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * '   ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            print('*** end of simulation time: {} events pending ***'.format(self.events.qsize()))
            pprint.pprint(self.temp_list)


def compute_duration(previous_action):
    if previous_action in ['leave garage', 'drop off passenger']:
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError(f'Unknown previous_action: {previous_action}')
    return int(random.expovariate(1 / interval)) + 1


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS, seed=None):
    if seed is not None:
        random.seed(seed)
    taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL) for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time', type=int,
                        default=DEFAULT_END_TIME,
                        help='simulation end time; default = %s'
                             % DEFAULT_END_TIME)
    parser.add_argument('-t', '--taxis', type=int,
                        default=DEFAULT_NUMBER_OF_TAXIS,
                        help='number of taxis running; default = %s'
                             % DEFAULT_NUMBER_OF_TAXIS)
    parser.add_argument('-s', '--seed', type=int, default=None, help='random generator seed (for testing)')
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)
