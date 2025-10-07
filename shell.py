import time
import readline
from parser import Parser
from lexer import Lexer

class Shell:

	def __init__(self):
		self._isRunning = True
		self._isTiming = False

		self.commands = {

			'exit' : [self.commandExit, 'Exits MLTS'],
			":help" : [self.commandHelp, 'Displays this help message'],
			'-f' : [self.commandFileRead, 'Reads and prints the contents of a file'],
			':timing' : [self.commandTiming, 'Toggle the execution timer'],
			':lex' : [self.commandLex, 'Displays the output of the lexer'],
			':parse' : [self.commandParse, 'Displays the output of the parser']
		}

	def commandExit(self, args):
		print('Exiting MLTS')
		self._isRunning = False

	def commandHelp(self, args):
		print('Available commands:')
		for command, message in self.commands.items():
			print(f'{command} : {message[1]}')

	def commandFileRead(self, args):
		filename = args[0]
		try:
			with open(filename, 'r') as file:
				print(file.read())

		except IndexError:
			print('Error: -f requires a filename')

		except FileNotFoundError:
			print(f'Error: The file {filename} could not be found')

		except Exception as e:
			print(f'Error: An unexcepted error has oocured: {e}')

	def commandTiming(self, args):
		self._isTiming = not(self._isTiming)
		status = 'enabled' if self._isTiming else 'disabled'
		print(f'Timing inputs is {status}.')

	def commandLex(self, args):
		if not args:
			print('Usage: :lex <expression>')
		
		try:
			inputString = ' '.join(args)
			lexer = Lexer(inputString)
			tokens = lexer.lex()
			print(tokens)

		except Exception as e:
			print(f'Error: {e}')

	def commandParse(self, args):
		if not args:
			print('Usage: :lex <expression>')

		try:
			inputString = ' '.join(args)
			lexer = Lexer(inputString)
			tokens = lexer.lex()

			parser = Parser(tokens)
			print(parser.parseProgram())

		except Exception as e:
			print(f'Error: {e}')


	def defaultHandler(self, inp):
		try:
			lexer = Lexer(inp)
			tokens = lexer.lex()

			parser = Parser(tokens)

			print(parser.prettyPrinting())

		except Exception as e:
			print(f'Error: {e}')


	def run(self):
		while self._isRunning:
			try:
				inp = input('MLTS> ')

				inpParts = inp.strip().split()
				command = inpParts[0]
				args = inpParts[1:]

				if command in self.commands:
					self.commands[command][0](args)

				else:
					self.defaultHandler(inp)
					
				if self._isTiming:
					startTime = time.perf_counter()

				if self._isTiming:
					endTime = time.perf_counter()
					print(f'Time elapsed: {(endTime - startTime):.6f}s')

			except KeyboardInterrupt:
				self.commandExit([])

			except EOFEError:
				self.commandExit([])

if __name__ == '__main__':
	shell = Shell()
	shell.run()
