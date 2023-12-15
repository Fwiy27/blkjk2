from utils.utils import clear_screen
from deck.deck import Deck
from dealer.logic import count, fix_hand, check_win
from dealer.display import get_bet_amount, print_board
from colorama import Fore

class Dealer:
    def __init__(self, number_of_decks=6):
        self.deck = Deck(number_of_decks)
        self.money = 5000
        self.bet_amount = 250
    
    def deal(self):
        self.dealer_hand = []
        self.user_hand = []
        for _ in range(2):
            self.dealer_hand.append(self.deck.draw())
            self.user_hand.append(self.deck.draw())

    def hit(self, user=True) -> int:
        if user:
            self.user_hand.append(self.deck.draw())
            self.user_hand = fix_hand(self.user_hand)
            if count(self.user_hand) > 21:
                return 2
            else:
                return 1
        else:
            self.dealer_hand.append(self.deck.draw())
            self.dealer_hand = fix_hand(self.dealer_hand)
            if count(self.dealer_hand) > 21:
                return 0
            else:
                return 4

    def play(self):
        while self.money > 0:
            clear_screen()
            status = 1
            self.bet_amount = get_bet_amount(self.money, self.bet_amount, len(self.deck.deck))
            self.deal()

            # Check initial dealer win
            status = check_win(self.dealer_hand, self.user_hand, True)
            if status == 2:
                self.dealer_hand = fix_hand(self.dealer_hand)


            # User
            while status == 1:
                clear_screen()
                print_board(self.dealer_hand, self.user_hand, self.money, self.bet_amount, True)
                choice = input('Choice: ')
                match choice:
                    case 's' | 'stand':
                        self.user_hand = fix_hand(self.user_hand)
                        status = 4
                    case 'h' | 'hit':
                        status = self.hit()
                    case 'clear':
                        clear_screen()
                        exit()
                    case _:
                        status = self.hit()

            # Dealer
            while status == 4:
                clear_screen()
                print_board(self.dealer_hand, self.user_hand, self.money, self.bet_amount)
                dealer_count = count(self.dealer_hand)
                if (isinstance(dealer_count, list) and max(dealer_count) >= 17) or (isinstance(dealer_count, int) and dealer_count >= 17):
                    self.dealer_hand = fix_hand(self.dealer_hand)
                    status = -1
                else:
                    status = self.hit(False)
                    input('Press Enter to Continue . . .')

            # After Game
            status = check_win(self.dealer_hand, self.user_hand)

            match status:
                case 0:
                    self.money += self.bet_amount
                    clear_screen()
                    print_board(self.dealer_hand, self.user_hand, self.money, self.bet_amount)
                    input(f'{Fore.GREEN}WON, Press Enter to Continue . . .{Fore.RESET}')
                case 2:
                    self.money -= self.bet_amount
                    if self.bet_amount > self.money:
                        self.bet_amount = self.money
                    clear_screen()
                    print_board(self.dealer_hand, self.user_hand, self.money, self.bet_amount)
                    input(f'{Fore.RED}LOST, Press Enter to Continue . . .{Fore.RESET}')