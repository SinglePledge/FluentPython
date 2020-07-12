import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]




beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print('---')
from random import choice

for i in range(3):
    print(choice(deck))
# slicing
print(deck[:3])
print(deck[12::13])

# 迭代
for card in deck:
    print(card)

print('-----')

# reversed
for card in reversed(deck):
    print(card)

#contains

print(Card('9','spands') in deck)
print(Card('9','spades') in deck)

#给牌添加权重
suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_values = FrenchDeck.ranks.index(card.rank)
    return rank_values * len(suits_values)+suits_values[card.suit]

#suits_value
for card in sorted(deck,key=spades_high):
    print(card)