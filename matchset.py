#----------------
# User Instructions
#
# The function, matchset, takes a pattern and a text as input
# and returns a set of remainders. For example, if matchset 
# were called with the pattern star(lit(a)) and the text 
# 'aaab', matchset would return a set with elements 
# {'aaab', 'aab', 'ab', 'b'}, since a* can consume one, two
# or all three of the a's in the text.
#
# Your job is to complete this function by filling in the 
# 'dot' and 'oneof' operators to return the correct set of 
# remainders.
#
# dot:   matches any character.
# oneof: matches any of the characters in the string it is 
#        called with. oneof('abc') will match a or b or c.

def matchset(pattern, text):
	"Match pattern at start of text; return a set of remainders of text."
	op, x, y = components(pattern)
	print op, x, y
	if 'lit' == op:
		#match the first and return the remainder. else return None
		print set([text[len(x):]]) if text.startswith(x) else null, "lit"
		return set([text[len(x):]]) if text.startswith(x) else null
	elif 'seq' == op:
		return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
	elif 'alt' == op:
		print matchset(x,text), 'matchx', matchset(y, text), 'my'
		print matchset(x, text) | matchset(y, text), "alt"
		return matchset(x, text) | matchset(y, text)
	elif 'dot' == op:
		print text[1:], 'dot'
		return set([text[1:]]) if text else null # your code here
	elif 'oneof' == op:
		print x
		return set([text[1:]]) if text[:1] == x else null # your code here
	elif 'eol' == op:
		return set(['']) if text == '' else null
	elif 'star' == op:
		return (set([text]) |
				set(t2 for t1 in matchset(x, text)
					for t2 in matchset(pattern, t1) if t1 != text))
	else:
		raise ValueError('unknown pattern: %s' % pattern)
		
null = frozenset()


def lit(s): return lambda text: set([text[len(s):]]) if text.startswith(s) else null


def seq(x, y): return lambda text: set().union(*map(y, x(text)))


def alt(x,y): return lambda text: x(text) | y(text)


def components(pattern):
    "Return the op, x, and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y


def test():
    assert matchset(('lit', 'abc'), 'abcdef')            == set(['def'])
    assert matchset(('seq', ('lit', 'hi '),
                     ('lit', 'there ')), 
                   'hi there nice to meet you')          == set(['nice to meet you'])
    assert matchset(('alt', ('lit', 'dog'), 
                    ('lit', 'cat')), 'dog and cat')      == set([' and cat'])
    assert matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
    assert matchset(('oneof', 'a'), 'aabc123')           == set(['abc123'])
    assert matchset(('eol',),'')                         == set([''])
    assert matchset(('eol',),'not end of line')          == frozenset([])
    assert matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])
    #e = seq(lit('hi'), lit('there '))
    #assert e('hi there nice to meet you') == set(['nice to meet you'])
    print "okay"
    print map(lit('there '), lit('hi')('hi there nice to meet you'))
    print "okay"
    #assert seq(lit('hi'), lit('there '))('hi there nice to meet you') == set(['nice to meet you'])
    g = alt(lit('a'), lit('b'))
    assert g('abc') == set(['bc'])
    
    return 'tests pass'

print test()

