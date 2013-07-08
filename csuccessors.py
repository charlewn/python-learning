# -----------------
# User Instructions
# 
# Write a function, csuccessors, that takes a state (as defined below) 
# as input and returns a dictionary of {state:action} pairs. 
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where 
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings: 
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C'
# where 'MM->' means two missionaries travel to the right side.
# 
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.
import time

def timeit(method):
	def timed(*args,**kw):
		ts= time.time()
		result = method(*args, **kw)
		te = time.time()
		print "name: %r (%r, %r) %2.7f sec" % \
			(method.__name__, args, kw, te-ts)
		return result
	return timed

@timeit
def csuccessors(state):
	"""Find successors (including those that result in dining) to this
	state. But a state where the cannibals can dine has no successors."""
	M1, C1, B1, M2, C2, B2 = state
	Mx = 2 # max number of people on the boat
	# your code here
	if C1 > M1 or C2 > M2:
		return {}
	print "Left side : {} Missorary, {} cannibal, {} boat".format(M1, C1, B1)
	print "Left side : {} Missorary, {} cannibal, {} boat".format(M2, C2, B2)
	if B1 > B2:
		#from left to right with (2,2,1,0,0,0)
		print dict(((M1-i,C1-j,B2,i,j,B1), "M"*i+"C"*j+"->")
				for i in range(M1+1)
				for j in range(C1+1)
				if i + j <= Mx and i + j != 0)
		return dict(((M1-i,C1-j,B2,M2+i,C2+j,B1), "M"*i+"C"*j+"->")
				for i in range(M1+1)
				for j in range(C1+1)
				if i + j <= Mx and i + j != 0)
	else:
		#from right to left
		return dict(((M1+i,C1+j,B2,M2-i,C2-j,B1), "<-"+"M"*i+"C"*j)
				for i in range(M2+1)
				for j in range(C2+1)
				if i+j <= Mx and i+j != 0)



def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C', 
                                               (2, 1, 1, 3, 3, 0): '<-M', 
                                               (3, 1, 1, 2, 3, 0): '<-MM', 
                                               (1, 3, 1, 4, 1, 0): '<-CC', 
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'


print test()