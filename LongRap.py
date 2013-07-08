# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(seq):
	current_count = 0
	max_count = 0
	
	if len(seq) == 0:
		return None
	else:
		store = seq[0]
		for i in range(1, len(seq)):
			if seq[i-1] == seq[i]:
				current_count = current_count + 1
				if current_count > max_count:
					max_count = current_count
					store = seq[i]
			else:
					current_count = 0
	
	return store
					



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([[1,1], [2,2], [2,2], [1,1]])
# None

print longest_repetition([[1,1], [2,2], [2,3], [1,1]])