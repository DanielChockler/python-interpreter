from lexer import Lexer

class Token:
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __repr__(self):
		return f'{self.type} {self.value}'

class SExpr:
	def __init__(self, contents):
		self.contents = contents

	def __repr__(self):
		res = ','.join(map(str, self.contents))
		return f'SExpr({res})'


class Parser:

	def __init__(self, inp):
		self.inp = inp
		self.pos = 0
		self.currentToken = self.inp[self.pos] if self.pos < len(self.inp) else None

	def getNextToken(self):
		# Advance token stream
		self.pos += 1

		if self.pos < len(self.inp):
			self.currentToken = self.inp[self.pos]

		else:
			self.currentToken = None

	def parseExpr(self):
		# If token is an opening bracket, start parsing the S expression
		if self.currentToken[1] == '(':
			return self.parseSExpr()

		# Finding a ')' here is an error
		elif self.currentToken[1] == ')':
			raise Exception('Unexpected closing bracket')

		else:
			atom = Token(self.currentToken[0], self.currentToken[1])
			self.getNextToken() # Consume current token
			return atom

	def parseSExpr(self):
		self.getNextToken() # Consume first '('

		res = []
		# Recursively call parseExpr() until finding ')'
		while self.currentToken is not None and self.currentToken[1] != ')':
			res.append(self.parseExpr())

		# Ran out of tokens before finding a closing bracket, so it's an error 
		if self.currentToken is None:
			raise Exception('Expected closing bracket')

		# Consume ')'
		self.getNextToken()

		return SExpr(res)

	def parseProgram(self):
		res = []

		while self.currentToken is not None:
			res.append(self.parseExpr())

		return res

	def prettyPrinting(self):
		ls = self.parseProgram() # Make sure there are no errors in input even when only pretty printing
		res = ''
		for i in self.inp:
			res += str(i[1]) + ' '

		return res
