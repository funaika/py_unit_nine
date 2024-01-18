
import random

class CardDeck:
    def __init__(self):
        self.suits = {
#code to make emojis colored from chat gpt
            "♠️": "black",
            "♥️": "red",
            "♦️": "red",
            "♣️": "black"
    }
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]        #define card values

        self.deck = [(value, suit) for value in self.values for suit in self.suits.keys()]      #creates deck of cards

    def shuffleCards(self):
#fisher-yates shuffle code from JenkinsDev on GitHub
        for i in range(len(self.deck) - 1, 0, -1):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

    def dealCards(self, numCards):
        if numCards * 2 > len(self.deck):
            raise ValueError("Not enough cards in the deck to deal.")

        player1Deck = self.deck[:numCards]
        player2Deck = self.deck[numCards:numCards*2]

        return player1Deck, player2Deck

