def slow_inverse(f, delta=1/128.):
	def f_1(y):
		x = 0
		while f(x) < y:
			x += delta
		return x if (abs(f(x)-y) < abs(f(x-delta)-y)) else x-delta
	return f_1
			


def slow_inverse(f, delta=1/1024.):
	def f_1(y):
		lo, hi = find_bounds(f, y)
		#print lo, hi
		return binary_search(f, y, lo, hi, delta)
	return f_1
	


def find_bounds(f, y):
	x = 1
	while f(x) < y:
		x = x*2.
	lo = 0 if (x == 1) else x/2.
	return lo, x


def binary_search(f, y, lo, hi, delta):
	while lo<= hi:
		x = (lo + hi)/2.
		print x
		if f(x) < y:
			lo = x + delta
		elif f(x) > y:
			hi = x - delta
		else:
			return x
	return hi if (abs(f(lo)-y) > abs(f(hi)-y)) else lo
	
	

def square(x): return x*x

sqrt = slow_inverse(square)

print sqrt(1000000000)

print 31622.7762307**2