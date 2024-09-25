import random

class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    @property
    def image_name(self):
        return f"{self.face.replace(' ', '_')}_{self.suit.replace(' ', '_')}.png"

    def __repr__(self):
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        return f"{self.face} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(face, suit) for face in Card.FACES for suit in Card.SUITS]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None


def play_matching_game():
    deck = Deck()
    player_card = deck.deal()
    print("player card")
    print(player_card)

play_matching_game()
