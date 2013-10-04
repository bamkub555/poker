def straight_flush(hand):
    '''
    (hand) -> bool

    Return True if hand is straight flush,
    return False if not
    '''
    return straight(hand) and flush(hand)
