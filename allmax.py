# -----------
# User Instructions
# 
# Write a function, allmax(iterable, key=None), that returns
# a list of all items equal to the max of the iterable, 
# according to the function specified by key. 


def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
	"Return a list of all items equal to the max of the iterable."
	# Your code here.
	#print iterable
	result, maxval = [], None
	key = key or (lambda x:x)
	n = 0
	for i in iterable:
		xval = key(i)
		if not result or maxval < key(i):
			result = [i]
			maxval = key(i)
		elif maxval == key(i):
			result.append(i)
		
	return result
	


def hand_rank_two(hand):
	"Return a value indicating the ranking of a hand."
	#print hand
	groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
	print groups
	#this will return 10, 10, 10 ,7, 7
	#print groups
	counts, ranks = unzip(groups)
	print counts, ranks
	#if ranks == ()
	


def group(items):
	"""return a list of [(count, x)...] highest count first, then highest x first"""
	groups = [(items.count(x), x) for x in set(items)]
	"""print set(items)
	print groups
	print "Hand %s" % items
	print groups
	print sorted(groups)
	print "Reversed %s" % sorted(groups, reverse=True)"""
	return sorted(groups, reverse=True)


def unzip(pairs):
	return zip(*pairs)

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has exactly n-of-a-kind of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def test():
	"Test cases for the functions in poker program."
	sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
	sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	tk1 = "3D 6D 3C 3H AS".split() #Three of a Kind
	assert poker([sf1, sf2, fk, fh]) == [sf1, sf2] 
	assert hand_rank_two(tk1) == (3, 1, 1)
	assert hand_rank_two(fh) == (6, 10, 7)
	return 'tests pass'


print test()
