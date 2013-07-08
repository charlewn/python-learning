# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def is_same(a, b):
	if a == b:
		return True
	else:
		return False

def longest_repetition(seq):
	if len(seq) == 0:
		return None
	else:
		prev = ''
		counter = 1
		winObj = []
		currentCounter = 0
		for obj in seq:
			if prev == '':
				prev = obj
				
			else:
				if is_same(prev, obj):
					counter = counter + 1
					if counter > currentCounter:
						currentCounter = counter
						winObj = obj
				else:
					prev = obj
					
					
		return winObj
		
	




#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

#print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
