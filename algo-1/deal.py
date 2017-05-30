simple_math = lambda x: x + 1

def allmax(iterable, key=None):
	result, maxval = [], None
	key = key or (lambda x: x)
	for x in iterable:
		xval = key(x)
		if not result or xval > maxval:
			result, maxval = [x], xval
		elif xval == maxval:
			result.append(x)
	return result


#[['6C', '7C', '8C', '9C', 'TC'], ['6D', '7D', '8D', '9D', 'TD'], 
#['9D', '9H', '9S', '9C', '7D'], ['TD', 'TC', 'TH', '7C', '7D']]