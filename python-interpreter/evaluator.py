from parser import SExpr, Token
import operator

class Function:
	def __init__(self, callable, arity):
		self.callable = callable
		self.arity = arity

	def __repr__(self):
		return f'<Function arity={self.arity}>'

class Evaluator:

	def __init__(self):
		self.functions = {
			'+' : Function(callable=operator.add, arity = 2),
			'-' : Function(callable=operator.sub, arity = 2),
			'*' : Function(callable=operator.mul, arity = 2),
			'/' : Function(callable=operator.truediv, arity =2),
		}

	def eval(self, expr):
		if not isinstance(expr, SExpr):
			return expr.value

		else:
			if not expr.contents:
				return expr

			function = expr.contents[0]
			args = expr.contents[1:]

			if function.value not in self.functions:
				raise Exception(f'Unkown function {function.value}')

			functionObj = self.functions[function.value]
			evaluatedArgs = [self.eval(arg) for arg in args]

			if len(evaluatedArgs) != functionObj.arity:
				raise Exception(f'Function {function.value} requires {functionObj.arity} arguments, but recieved {len(evaluatedArgs)}')

			return functionObj.callable(*evaluatedArgs)