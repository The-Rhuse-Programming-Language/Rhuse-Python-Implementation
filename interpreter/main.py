from tokenizer import *
from parser import *
import sys
with open(input("<usage> Enter .rh script (must be in current directory)\n"), 'r')as script:
	for line in script.read():
		parse(tokenize(line))