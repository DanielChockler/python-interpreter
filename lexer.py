class Lexer:

	def __init__(self, inp):
				
		self.inp = inp
		self.position = 0
		self.currentChar = self.inp[self.position] if self.position < len(self.inp) else None
		self.tokenTypes = {

			int : 'INT',
			float : 'FLOAT',
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
		dotCount = 0

		while self.currentChar is not None and (self.currentChar.isdigit() or self.currentChar == '.'):
			if self.currentChar == '.':
				if dotCount == 1:
					break
				dotCount += 1

			returnNum += self.currentChar
			self.getNextChar()

		if dotCount == 1:
			if returnNum == '.':
				return ['STRING', '.']
			return [self.tokenTypes[float], float(returnNum)]

		else:
			return [self.tokenTypes[int], int(returnNum)]

	def getString(self):
		returnStr = ''

		while self.currentChar is not None and not(self.currentChar.isspace()) and not(self.currentChar.isdigit()) and not(self.currentChar in self.tokenTypes):
			returnStr += self.currentChar
			self.getNextChar()

		return returnStr


	def generateToken(self):
		while self.currentChar is not None:

			if self.currentChar.isspace():
				self.getNextChar()
				continue

			if self.currentChar.isdigit() or self.currentChar == '.':
				if self.currentChar == '.' and (self.position + 1 >= len(self.inp) or not self.inp[self.position + 1].isdigit()):
					char = self.currentChar
					self.getNextChar()
					return ['SYMBOL', char]

				return self.getNumber()

			elif self.currentChar in self.tokenTypes:
				char = self.currentChar
				self.getNextChar()
				return [self.tokenTypes[char], char]

			else:
				return ['STRING', self.getString()]

		return 'EOF'

	def lex(self):
		returnList = []
		while True:
			token = self.generateToken()
			if token == 'EOF':
				break

			returnList.append(token)

		return returnList
