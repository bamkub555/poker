def straight_flush(hand):
    '''
    (hand) -> bool

    Return True if hand is straight flush,
    return False if not
    '''
    return straight(hand) and flush(hand)

def straight(hand):
    return None

def flush(hand):
    suits = []
    for r,s in hand:
        suits.append(s)
    return len(set(suits)) == 1

