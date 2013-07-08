# -----------------
# User Instructions
# 
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes 
# as input capacities, goal, and (optionally) start. This function should 
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the 
# volume of a glass. 
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty). 
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i), 
# ('empty', i), ('pour', i, j) where i and j are indices indicating the 
# glass number. 

import itertools

def more_pour_problem(capacities, goal, start=None):
	"""The first argument is a tuple of capacities (numbers) of glasses; the
	goal is a number which we must achieve in some glass.  start is a tuple
	of starting levels for each glass; if None, that means 0 for all.
	Start at start state and follow successors until we reach the goal.
	Keep track of frontier and previously explored; fail when no frontier.
	On success return a path: a [state, action, state2, ...] list, where an
	action is one of ('fill', i), ('empty', i), ('pour', i, j), where
	i and j are indices indicating the glass number."""
	# your code here
	if start == None: start = (0,)*len(capacities)
	indices = range(len(capacities))
	single_action = [(motion, i) for motion in ['fill','empty'] for i in indices]
	pouring = [("pour", i, j) for i in indices for j in indices if i !=j]
	def is_goal(state): return goal in state

	def psuccessors(state):
		new_states = {}
		for (action, index) in single_action:
			if action is 'empty':
				new_states[replace(state, index, 0)] = (action, index)
			if action is 'fill':
				new_states[replace(state, index, capacities[index])] = (action, index)
		for (action, i, j) in pouring:
			amount = min(state[i], capacities[j] - state[j])
			state2 = replace(state, i, state[i] - amount)
			new_states[replace(state2, j, state[j]+amount)] = (action, i, j)
		return new_states
		
	return shortest_path_search(start, psuccessors, is_goal)
	
def replace(seq, i, val):
	s = list(seq)
	s[i] = val
	return type(seq)(s)


def more_pour_problem2(capacities, goal, start=None):
	"""The first argument is a tuple of capacities (numbers) of glasses; the
	goal is a number which we must achieve in some glass.  start is a tuple
	of starting levels for each glass; if None, that means 0 for all.
	Start at start state and follow successors until we reach the goal.
	Keep track of frontier and previously explored; fail when no frontier.
	On success return a path: a [state, action, state2, ...] list, where an
	action is one of ('fill', i), ('empty', i), ('pour', i, j), where
	i and j are indices indicating the glass number."""
	# your code here
	def is_goal(state): return goal in state
	
	#print capacities
	if start is None: start = (0,)*len(capacities)
	def psuccussors(state):
		#return all the state fill, i, empty, i pour, i, j, state, action
		#[(0,0,0,0),('fill', 2), (0,0,4,0)] 
		#indices = [i[0] for i in enumerate(state)] #range(len(state))
		succ = {}
		def pour(i, j):
			#(0, 1)
			#state[0] = 0, capacities[1] = 2 - state[0] = 0
			amount = min(state[i], capacities[j]- state[j])
			
			newstate = list(state)
			newstate[i] -= amount
			newstate[j] += amount
			return tuple(newstate[:-1]) #remove reservoir when returning
		
		state = state + (reservoir,)
		for i, j in itertools.permutations(range(n+1),2): #(5 npr 2), n = 4
			print (i, j)
			succ[pour(i,j)] = ('fill', j) if i == n else \
							('empty', i) if j == n else \
							('pour', i, j)
		return succ
		
	n = len(capacities)
	
	reservoir = max(capacities)
	capacities = capacities + (reservoir*2,)
		
	return shortest_path_search(start, psuccussors, is_goal)

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [ [start] ] 
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []
    
def test_more_pour():
    assert more_pour_problem((1, 2, 4, 8), 4) == [
        (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    assert more_pour_problem((1, 2, 4), 3) == [(0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)] 
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28) == []
    return 'test_more_pour passes'

print test_more_pour()