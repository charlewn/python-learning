# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
	"Return (i, j) such that text[i:j] is the longest palindrome in text."
	# Your code here
	if len(text) == 0:
		return (0,0)
	length, text = len(text), text.lower()
	start = [(i,i) for i in range(length+1)] + [(i, i+1) for i in range(length)]
	pals = []
	while start:
		start = [(i-1, j+1) for (i, j) in start if i > 0 and j <length and text[i-1] == text[j]]
		if start:
			pals = start
	longest = lambda (x, y) : y - x
	return max(pals, key=longest)


def grow(start, end, text):
	#(4,4), (5,6), (3,4)
	#pals = [(i,j) for i]
	#if text[start] == text[end]:
	pass
		


def test():
	L = longest_subpalindrome_slice
	assert L('racecar') == (0, 7)
	assert L('Racecar') == (0, 7)
	assert L('RacecarX') == (0, 7)
	assert L('Race carr') == (7, 9)
	assert L('') == (0, 0)
	assert L('something rac e car going') == (8,21)
	assert L('xxxxx') == (0, 5)
	assert L('Mad am I ma dam.') == (0, 15)
	return 'tests pass'


print test()