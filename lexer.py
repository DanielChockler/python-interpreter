class Lexer:

	def __init__(self, inp):
		self.inp = inp
		self.position = 0
		self.currentChar = self.inp[self.position] if self.position < len(self.inp) else None
		self.tokenTypes = {

			int : 'NUMBER',
			'+' : 'PLUS',
			'-' : 'MINUS',
			'*' : 'MULTIPLY',
			'/' : 'DIVIDE',
			'(' : 'LPAREN',
			')' : 'RPAREN'

		}

	def getNextChar(self):
		self.position += 1
		if self.position >= len(self.inp):
			self.currentChar = None

		else:
			self.currentChar = self.inp[self.position]

	def getNumber(self):
		returnNum = ''

		while self.currentChar is not None and self.currentChar.isdigit():
			returnNum += self.currentChar
			self.getNextChar()

		self.position -= 1
		return int(returnNum)


	def generateToken(self):
		while self.currentChar is not None:

			if self.currentChar.isspace():
				self.getNextChar()
				continue

			if self.currentChar.isdigit():
				return [self.tokenTypes[int], self.getNumber()]

			elif self.currentChar in self.tokenTypes:
				return [self.tokenTypes[self.currentChar], self.currentChar]

			else:
				raise Exception(f'Invalid character: {self.currentChar}')

		return 'EOF'

	def lex(self):
		returnList = []
		while True:
			token = self.generateToken()
			if token == 'EOF':
				break

			returnList.append(token)
			self.getNextChar()

		return returnList

inp = '5+2'
lexer = Lexer(inp)
print(lexer.lex())
