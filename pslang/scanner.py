import shlex
import stack
import os

class Scanner(stack.Stack):
	'''	'''
	def __init__(self, file=None):
		'''	'''
		if file == None:
			raise exceptions.InvalidArgs
		stack.Stack.__init__(self)
		self.lexxer = shlex.shlex(instream=open(file, 'r'))
		try:
			while 1:
				self.push(self.lexxer.next())
		except StopIteration:
			pass

