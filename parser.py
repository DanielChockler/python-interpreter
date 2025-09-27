from lexer import Lexer

class Parser:

	def __init__(self, inp):
		self.inp = inp
		self.pos = 0
		self.currentToken = self.inp[self.pos] if self.pos < len(self.inp) else None

	def getNextToken(self):
		self.pos += 1

		if self.pos < len(self.inp) and self.inp[self.pos] is not None:
			self.currentToken = self.inp[self.pos]

		else:
			self.currentToken = None

	def parseExpr(self):
		if self.currentToken[1] == '(':
			return self.parseSExpr()

		elif self.currentToken[1] == ')':
			raise Exception('Unexpected closing bracket')

		else:
			return self.currentToken

	def parseSExpr(self):
		self.getNextToken()
		SExpr = '('
		res = ['SEXPR']
		subExpr = []
		try:
			while self.currentToken[1] != ')':

				if self.currentToken[1] == '(':
					subExpr.append(self.parseSExpr())

				SExpr += str(self.currentToken)

				self.getNextToken()
			SExpr += ')'
			res.append(SExpr)
			res.extend(subExpr)

			return res

		except TypeError:
			raise Exception('Expected closing bracket')

	def parseProgram(self):
		res = []

		while self.pos < len(self.inp) and self.currentToken is not None:
			if self.currentToken[0] == 'SYMBOL':
				res.append(self.parseExpr())

			else:
				res.append(self.currentToken)

			self.getNextToken()

		return res

inp = '(5 + 5 + (10 + 2)) + he()'
lexer = Lexer(inp)
inp = lexer.lex()

parser = Parser(inp)
print(parser.parseProgram())