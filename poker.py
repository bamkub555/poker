def all_max(hands):
    '''
    (hands)-> list
    Return list of max rank hand
    or hands if max rank hand has more than one
    '''
    winhand = max(hands, key=hand_rank)
    maxval = hand_rank(winhand)
    result = []
    for hand in hands:
        if hand_rank(hand) == maxval:
            result.append(hand)
    return result

def hand_rank(hand):
    '''
    (hand)-> tuple
    Return the hand rank of this hand
    '''
    ranks = []
    for r,s in hand:
        ranks.append('--23456789TJQKA'.index(r))
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
    if straight_flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks)
    elif full_house(ranks):
        return 6, kind(3, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(hand):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks)
    elif twopair(ranks):
        return 2, twopair(ranks)[0], twopair(ranks)[1], kind(1, ranks)
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks
        
def straight_flush(hand):
    '''
    (hand) -> bool

    Return True if hand is straight flush or False if not
    '''
    return straight(hand) and flush(hand)

def straight(hand):
    '''
    (hand) -> bool
    
    Return True if hand is straight or False if not
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

    Return True if hand is flush or False if not 
    '''
    suits = []
    for r,s in hand:
        suits.append(s)
    return len(set(suits)) == 1

def full_house(ranks):
    '''
    (ranks) -> bool

    Return True if hand is full_house or False if not
    '''
    
    return True if kind(3, ranks) and kind(2, ranks) else False

def kind(n,ranks):
    '''
    (n, ranks) -> int

    Return rank if hand is n kind or 0 if not
    '''
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return 0

def twopair(ranks):
    '''
    (ranks) -> tuple

    Return tuple of highpair and lowpair
    or empty tuple if ranks is not twopair
    '''
    ranks.sort(reverse=True)
    high_pair = kind(2, ranks)
    ranks.sort()
    low_pair = kind(2, ranks)
    ranks.sort(reverse=True)
    if high_pair != low_pair:
        return (high_pair, low_pair)
    return ()
        



    


