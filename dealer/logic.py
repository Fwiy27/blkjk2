from deck.deck import is_ace

def count_aces(hand) -> int:
    count = 0
    for card in hand:
        count += 1 if isinstance(card[1], list) else 0
    return count

def count(hand) -> int:
    num_aces = count_aces(hand)
    count = 0
    count2 = 0
    count3 = 0

    if num_aces == 0:
        for card in hand:
            count += card[1]
        return count
    elif num_aces == 1:
        for card in hand:
            if is_ace(card):
                count += card[1][0]
                count2 += card[1][1]
            else:
                count += card[1]
                count2 += card[1]
        return [count, count2]
    else:
        return 12
    
def fix_hand(hand) -> list:
    num_aces = count_aces(hand)
    if num_aces == 0:
        return hand
    elif num_aces == 1:
        value = 1 if (max(count(hand)) <= 21) else 0
        for i in range(len(hand)):
            if is_ace(hand[i]):
                hand[i][1] = hand[i][1][value]
        return hand
    elif num_aces == 2:
        changed_aces = 0
        for i in range(len(hand)):
            if is_ace(hand[i]):
                hand[i][1] = hand[i][1][changed_aces]
                changed_aces += 1
        return hand
    else:
        changed_aces = 0
        for i in range(len(hand)):
            hand[i][1] = hand[i][1][changed_aces]
            changed_aces = not changed_aces
        return hand
    
def check_win(dealer_hand, user_hand, first = False) -> int:
    # 0 = Win, 1 = Keep Playing, 2 = Lose, 4 = Check Game
    dealer_count = count(dealer_hand)
    user_count = count(user_hand)
    
    if first:
        print(dealer_count)
        return 2 if (isinstance(dealer_count, list) and max(dealer_count) == 21) else 1
    
    if user_count > 21:
        return 2
    if dealer_count > 21 and user_count <= 21:
        return 0
    elif dealer_count == 21:
        return 2
    elif dealer_count >= user_count:
        return 2
    elif user_count > dealer_count:
        return 0
    else:
        return 1