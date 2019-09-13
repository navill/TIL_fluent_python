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


deck = FrenchDeck()

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# suit_values에 가중치를 구현하고 이를 아래의 함수를 이용해 정렬의 기준이 되는 값을 구할 수 있다.
def spades_high(card):  # card -> deck._cards
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(rank_value * len(suit_values) + suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


# print(deck.ranks, deck.suits)
for card in sorted(deck, key=spades_high):
    print(card)
