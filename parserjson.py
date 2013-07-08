from functools import update_wrapper
from string import split
import re

def grammar(description, whitespace=r'\s*'):
	G = { ' ': whitespace}
	description = description.replace('\t', ' ')
	for line in split(description, '\n'):
		lhs, rhs = split(line, ' => ', 1)
		alternatives = split(rhs, ' | ')
		G[lhs] = tuple(map(split, alternatives))
	
	print G


print grammar("Symbol =>  A1 A2")