import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


# rank, suit 속성을 갖는 Card 클래스가 생성된다.

class FrenchDeck:
    ranks = [str(c) for c in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        # print(self._cards)

    def __len__(self):
        return len(self._cards)

    # data[0], data[1] 등 배열의 위치에 있는 데이터를 가져오는 기능 __getitem__()메서드가 제공한다.
    # self._cards의 [] 연산자에 작업을 위임함으로써 list에서 제공하는 기능(slicing 포함)을 사용할 수 있다.
    def __getitem__(self, position):
        return self._cards[position]


from random import shuffle

deck = FrenchDeck()
# 현재 FrenchDeck은 namedtuple(불변 객체)를 갖기 때문에 가변 객체를 사용하는
# shuffle의 인자로 사용할 경우 에러를 일으킨다.
shuffle(deck)  # -> 에러 발생


# 아래와 같이 __setitem__시그니처와 동일하고 가변 객체를 생성하는 함수를 만들고
# FrenchDeck.__setitem__ 속성에 전달함으로써 FrenchDeck 객체를 이용한
# shuffle을 동작시킬 수 있다.
def set_card(self, key, value):
    self._cards[key] = value


# 런타임시 객체의 속성을 변경하고 다른 동작을 실행 시킬 수 있도록 변경하는 것을
# 멍키 패칭이라고 한다.
FrenchDeck.__setitem__ = set_card
deck2 = FrenchDeck()

shuffle(deck2)

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(c) for c in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # shuffle에서 사용될 가변 객체 생성
    def __setitem__(self, position, value):
        self._cards[position] = value

    # collections.MutableSequence의 추상메서드인 __deltime__과 insert를 구현해야한다.
    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)
