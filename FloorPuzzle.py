#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
	# Your code here
	floor = [1,2,3,4,5]
	orderings = itertools.permutations(floor, 5)
	#print orderings
	for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
		if Hopper != 5 and Kay != 1: 
			if Liskov != 5 and Liskov != 1:
				if Perlis > Kay:
					if not next_to(Ritchie,Liskov) and not next_to(Liskov, Kay):
						result = [Hopper, Kay, Liskov, Perlis, Ritchie]
	return result


def next_to(a, b):
	return True if abs(a-b) == 1 else False

print floor_puzzle()