
def pendulum(num):
	number = str(num)
	# print(number[-1])
	result = True
	length = len(number)
	if length % 2 == 1: # odd
		length = length - 1
		for i in range(0, int(length/2)):
			if number[i] != number[length-i]:
				result = False
			
	elif length % 2 == 0: # even
		for i in range(0, int(length/2)):
			if number[i] != number[length-i-1]:
				result = False

	return result

assert pendulum(1221) == True
assert pendulum(123321) == True
assert pendulum(12345) == False
assert pendulum(1263621) == True
assert pendulum(122333221) == True
print("all pass")