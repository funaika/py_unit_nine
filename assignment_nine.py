import random
from deck import CardDeck

def compareCards(card1, card2, deck):
    value1, suit1 = card1
    value2, suit2 = card2

    if deck.values.index(value1) > deck.values.index(value2):
        return 1
    elif deck.values.index(value1) < deck.values.index(value2):
        return 2
    else:
        return 0

numRounds = int(input("Enter the number of rounds to play: "))
def playWar(numRounds):
    deck = CardDeck()
    deck.shuffleCards()
    player1Deck, player2Deck = deck.dealCards(2 * numRounds)

    roundsPlayed = 0

    while player1Deck and player2Deck and roundsPlayed < numRounds:
        if not player1Deck or not player2Deck:
            break

        player1Card = player1Deck.pop(0)
        player2Card = player2Deck.pop(0)

        result = compareCards(player1Card, player2Card, deck)

        print(f"Player 1: {player1Card}  vs  Player 2: {player2Card}")

        if result == 1:
            print("Player 1 wins the round!")
            player1Deck.extend([player1Card, player2Card])
        elif result == 2:
            print("Player 2 wins the round!")
            player2Deck.extend([player1Card, player2Card])
        else:
            print("Tie!")

        roundsPlayed += 1

    if len(player1Deck) > len(player2Deck):
        print("Player 1 wins the game!")

    elif len(player1Deck) < len(player2Deck):
        print("Player 2 wins the game!")
    else:
        print("It's a tie!")

playWar(numRounds)
