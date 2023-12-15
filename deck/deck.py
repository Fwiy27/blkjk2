import random
from colorama import Fore

suits = ['♠', '♥', '♦', '♣']
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def is_ace(card) -> bool:
    return True is isinstance(card[1], list)

def get_value(card) -> int:
    if card[0] in ['A', 'J', 'Q', 'K', '10']:
        match card[0]:
            case 'A':
                return [1, 11]
            case _:
                return 10
    else:
        return int(card[0])

def pretty(card) -> str:
    if card[-1] in ['♥', '♦']:
        return (Fore.RED + card + Fore.RESET)
    else:
        return (Fore.LIGHTBLACK_EX + card + Fore.RESET)

class Deck:
    def __init__(self, number_of_decks=1):
        self.shuffle(number_of_decks)
    
    def shuffle(self, num) -> None:
        # Empty Deck
        self.deck = []

        # Add Cards to Deck
        for _ in range(num):
            for suit in suits:
                for face in faces:
                    self.deck.append(face+suit)

    def draw(self) -> str:
        if len(self.deck) == 0:
            self.shuffle()

        index = random.randint(0, len(self.deck) - 1)
        card = self.deck[index]
        self.deck.pop(index)
        return [card, get_value(card)]