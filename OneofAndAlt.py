# --------------
# User Instructions
#
# Complete the code for the compiler by completing the constructor
# for the patterns alt(x, y) and oneof(chars). 

def lit(s):         return lambda Ns: set([s]) if len(s) in Ns else null
def alt(x, y):      return lambda Ns: x(Ns) | y(Ns)
def star(x):        return lambda Ns: opt(plus(x))(Ns)
def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1) #Tricky
def oneof(chars):   return lambda Ns: set(chars) if 1 in Ns else null
def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
def opt(x):         return alt(epsilon, x)
dot = oneof('?')    # You could expand the alphabet to more chars.
epsilon = lit('')   # The pattern that matches the empty string.

null = frozenset([])
def genseq(x, y, Ns):
	print oneof('bcfhrsm')
	Nss = range(max(Ns)+1)
	print Ns, Nss
	return set(m1 + m2 for m1 in x(Nss) for m2 in y(Nss) if len(m1 + m2) in Ns)	

def test():
    
    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4]))    == null 
    
    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])
    
    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null
    a,b,c = map(lit, 'abc')    
    i = seq(oneof('bcfhrsm'),lit('at'))
    print i(set([3]))
    assert i(set([3])) == set(['bat','cat','fat', 'mat', 'rat','hat', 'sat'])
    return 'tests pass'

print test()