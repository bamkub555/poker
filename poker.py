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
    ranks = []
    for r,s in hand:
        ranks.append('--23456789TJQKA'.index(r))
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
    return max(ranks)-min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
    '''
    (hand) -> bool

    Return True if hand is flush,
    return False  if not 
    '''
    suits = []
    for r,s in hand:
        suits.append(s)
    return len(set(suits)) == 1




