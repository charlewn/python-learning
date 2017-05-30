# -----------------
# User Instructions
# 
# Write the two action functions, hold and roll. Each should take a
# state as input, apply the appropriate action, and return a new
# state. 
#
# States are represented as a tuple of (p, me, you, pending) where
# p:       an int, 0 or 1, indicating which player's turn it is.
# me:      an int, the player-to-move's current score
# you:     an int, the other player's current score.
# pending: an int, the number of points accumulated on current turn, not yet scored

def hold(state):
	"""Apply the hold action to a state to yield a new state:
	Reap the 'pending' points and it becomes the other player's turn."""
	# your code here
	(p, me, you, pending) = state
	new_state = ()
	if state[0] == 0:
		new_state = (1, state[2], state[1]+state[3], 0)
	else:
		new_state = (0, state[2], state[1]+state[3], 0)
	return new_state

def roll(state, d):
	"""Apply the roll action to a state (and a die roll d) to yield a new state:
	If d is 1, get 1 point (losing any accumulated 'pending' points),
	and it is the other player's turn. If d > 1, add d to 'pending' points."""
	# your code here
	lst = list(state)
	if d == 1:
		lst[3] = 1
		return hold(tuple(lst))
	else:
		lst[3] = lst[3] + d
		return tuple(lst)
    
def test():    
    assert hold((1, 10, 20, 7))    == (0, 20, 17, 0)
    assert hold((0, 5, 15, 10))    == (1, 15, 15, 0)
    assert roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)
    assert roll((0, 5, 15, 10), 5) == (0, 5, 15, 15)
    return 'tests pass'

print test()