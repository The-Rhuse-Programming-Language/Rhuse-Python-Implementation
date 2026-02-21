from tokenizer import *
from parser import *
import sys
if sys.argv[1]:
	with open(sys.argv[1], 'r') as script:
		for line in script.read():
			parse(tokenize(line))
else:
	print("<usage>: python main.py script.rh")
