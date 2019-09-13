class Demo:
    @classmethod
    def klassmeth(*args):
        return args #
    @staticmethod
    def statmeth(*args):
        return args #

print(Demo.klassmeth())  # (<class '__main__.Demo'>,)
print(Demo.klassmeth('a'))  # (<class '__main__.Demo'>, 'a')
print(Demo.statmeth())  # ()
print(Demo.statmeth('a'))  # ('a',)
