def genseq(x, y, Ns):
	Nss = range(max(Ns)+1)
	return set(m1 + m2 for m1 in x(Nss) for m2 in y(Nss) if len(m1 + m2) in Ns)	


def lit(s): return lambda text: set([text[len(s):]]) if text.startswith(s) else null


def test():
	assert genseq(lit('hi'), lit('there '), 'hi there nice to meet you')
	return 'tests pass'


print test()