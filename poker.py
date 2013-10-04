def straight_flush(hand):
    '''
    (hand) -> bool

    Return True if hand is straight flush,
    return False if not
    '''
    return straight(hand) and flush(hand)

def straight(hand):
    '''
    (hand) -> bool
    
    Return True if hand is straight,
    return False if not
    '''
    return None

def flush(hand):
    '''
    (hand) -> bool

    Return True if hand is flush,
    reture False  if not 
    '''
    suits = []
    for r,s in hand:
        suits.append(s)
    return len(set(suits)) == 1



