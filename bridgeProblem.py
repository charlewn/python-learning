# -----------------
# User Instructions
# 
# Modify the bridge_problem(here) function so that it 
# tests for goal later: after pulling a state off the 
# frontier, not when we are about to put it on the 
# frontier.

def bsuccessors(state):
	"""Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
	where here and there are frozensets of people (indicated by their times) and/or
	the light, and t is a number indicating the elapsed time."""
	here, there, t = state
	#print here, there, t
	if 'light' in here:
		return dict(((here - frozenset([a,b, 'light']),
				 	there | frozenset([a,b, 'light']),
					(max(a,b)+t)), (a, b, '->'))
					for a in here if a is not 'light'
					for b in here if b is not 'light' and a<=b)
	else:
		return dict(((here | frozenset([a,b, 'light']),
				there - frozenset([a,b, 'light']),
				(max(a,b)+t)), (a,b, '<-'))
				for a in there if a is not 'light'
				for b in there if b is not 'light')
	


def path_states(path):
	#print path[::2]
	return path[::2]


def path_actions(path):
	return path[1::2]


def elapsed_time(path):
	return path[-1][2]

def bridge_problem(here):
	here = here | frozenset(['light'])
	explored = set()
	frontier = [[(here, frozenset([]), 0)]]
	print 'frontier: ', frontier
	if not here:
		return frontier[0]
	while frontier:
		path = frontier.pop(0)
		print "path: ", path 
		here1, there1, t1 = path[-1]
		if not here1 or here1 == set(['light']):
			return path
		for (state, action) in bsuccessors(path[-1]).items():
			#print 'state: ', state, 'action: ', action
			if state not in explored:
				here, there, t = state
				explored.add(state)
				#print "here: %r, there: %r, t: %r" % \
						#(here, there, t)
				path2 = path + [action, state]
				frontier.append(path2)
				frontier.sort(key=elapsed_time)
	return Fail

Fail = []




def test():
	"""assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
			(frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}
	assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
			(frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}"""
	testpath = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
				(5, 2, '->'),                                        # action 1
				(frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
				(2, 1, '->'),                                        # action 2
				(frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
				(5, 5, '->'), 
				(frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
				(5, 10, '->'), 
				(frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
				(2, 2, '->'), 
				(frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
				(10, 1, '->'), 
				(frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
				(10, 10, '->'), 
				(frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
				(10, 2, '->'), 
				(frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
				(5, 1, '->'), 
				(frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
				(1, 1, '->')]
	assert path_states(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
		(frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
		(frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
		(frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
		(frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
		(frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
		(frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
		(frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
		(frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
		(frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
	assert path_actions(testpath) == [(5, 2, '->'), # action 1
		(2, 1, '->'), # action 2
		(5, 5, '->'), 
		(5, 10, '->'), 
		(2, 2, '->'), 
		(10, 1, '->'), 
		(10, 10, '->'), 
		(10, 2, '->'), 
		(5, 1, '->'), 
		(1, 1, '->')]
	print bridge_problem(frozenset((1, 2),))[-1][-1]
	assert bridge_problem(frozenset((1, 2),))[-1][-1] == 2 # the [-1][-1] grabs the total elapsed time
	assert bridge_problem(frozenset((1, 2, 5, 10),))[-1][-1] == 17
	return 'tests pass'


print test()