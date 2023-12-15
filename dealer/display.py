from deck.deck import pretty, get_value
from dealer.logic import count
from colorama import Fore
from utils.utils import clear_screen

def pretty_hand(hand, hidden = False) -> str:
    s = ''
    if hidden:
        s += f'[{pretty(hand[0][0])}][?]'
    else:
        for card in hand:
            s += f'[{pretty(card[0])}]'
    return s

def print_hand(hand, who, hidden = False):
    value = count(hand) if not hidden else get_value(hand[0][0])
    print(f'[{who}]: {pretty_hand(hand, hidden)} | {value}')

def get_bet_amount(money, current_bet_amount, cards) -> int:
    print(f"{Fore.GREEN}Money: ${money}{Fore.RESET}")
    print(f"{Fore.RED}Current Bet: ${current_bet_amount}{Fore.RESET}")
    print(f"Cards Remaining: {cards}")
    bet = input("Bet: ")
    if bet in ['all', 'half', 'clear']:
        match bet:
            case 'all':
                return money
            case 'half':
                return int(money/2)
            case 'clear':
                clear_screen()
                exit()
    try:
        return int(bet)
    except:
        return current_bet_amount

def print_board(dealer_hand, user_hand, money, bet_amount, hidden = False):
    print(f'{Fore.GREEN}Money: ${money}{Fore.RESET} | {Fore.RED}Bet: {bet_amount}{Fore.RESET}')
    print_hand(dealer_hand, "DEALER", hidden)
    print_hand(user_hand, "USER")