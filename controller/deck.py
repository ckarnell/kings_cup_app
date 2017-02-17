import random

class Deck:
    def __init__(self):
        self.deck = range(52)
        random.shuffle(self.deck)

    def newDeck(self):
        self.deck = range(52)
        random.shuffle(self.deck)

    def getCard(self):
        if(len(self.deck) == 0):
            print 'Out of cards. Shuffling a new deck.'
            self.newDeck()

        card = self.deck[0]
        self.deck = self.deck[1:]
        cardRep = {'val': '', 'suit': '', 'num': card}

        # Set the value of the card.
        face = {0: 'J', 1: 'Q', 2: 'K'}
        val = card % 13
        if val >= 10:
            cardRep['val'] += face[val % 10]
        elif val == 0:
            cardRep['val'] += 'A'
        else:
            cardRep['val'] += str(val + 1)

        # Set the suit of the card.
        suit = {0: 'S', 1: 'C', 2: 'H', 3: 'D'}
        cardRep['suit'] += suit[card / 13]

        return cardRep
