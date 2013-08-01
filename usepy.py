#
# Useful Funcs #
#
import itertools
import sys
import time
import random

def randInts():
	while True:
		sys.stdout.write(str(random.randint(0,9)))
		sys.stdout.flush()
		time.sleep(0.1)

def spin():
	for x in itertools.cycle('|\-/'):
		sys.stdout.write('\r' + x)
		sys.stdout.flush()
		time.sleep(0.1)

def fonetic(pword):
	# pword = 'br549ZQR'
	spacer = " "    # character to use between words.
	dij = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Niner', '0':'Zero'}
	alf = {'a':'alpha', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliet', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}
	pun = {'-': 'dash', '&': 'ampersand', '@': 'at-sign', '.': 'dot', ',': 'comma', '!': 'exclamation', 
		'#': 'pound', ':': 'colon', ';': 'semicolon', '%': 'percent', '*': 'asterisk', '$': 'dollar',
		'^': 'caret', '(': 'left-parens', ')': 'right-parens', '\\': 'backslash', '_': 'underbar',
		'-': 'minus', '+': 'plus', '=': 'equals', '{': 'left brace', '}': 'right brace', '[': 'left bracket',
		']': 'right bracket', '|': 'pipe', '"': 'double-quote', '<': 'less than', '>': 'greater than',
		'?': 'question', '/': 'forward slash', '\'': 'single quote', '~': 'tilde', '`': 'back quote', ' ': 'space' }  
	# print '\nPassword: ' + pword
	s = ''    # create a blank string
	for foo in pword:
		if foo.isdigit():
			s += dij[foo] 
		elif foo.islower():
			s += alf[foo] 
		elif foo.isupper():
			s += alf[foo.lower()].upper()
		else:
			try:
				s += '[' + pun[foo] + ']'
			except KeyError:
				s += '"' + foo + '"'
		s += spacer
	 # print '\nPhonetic: ' + s[:-1]
	return s[:-1]

colors = {'pink': '\033[95m', # for use with stdout. always end with color['black'] or 'res'
			'blue': '\033[94m',
			'green': '\033[92m',
			'yellow': '\033[93m',
			'red': '\033[91m',
			'black': '\033[0m',
			'res': '\033[0m'}
def showColors():
	i=0
	while i<110:
		sys.stdout.write('\033['+str(i)+'mABCDEFG - '+str(i)+'\033[0m\n')
		sys.stdout.flush()
		time.sleep(0.1)
		i+=1
	sys.stdout.write(colors['black']+'\\033[#m\n')

def p(m,k,d=1): #One Time Pad. ('text', listOfNum/range(), True if decrypting)
	return "".join([chr((ord(c)-ord('a')+i*(-1)**d)%26 + ord('a')) for c,i in zip(m,k)])


