import lexxer, stack 
import os

class Scanner(lexxer.Lexxer, stack.Stack):
	'''	'''
	def __init__(self, file=None):
		'''	'''
		if file == None:
			raise exceptions.InvalidArgs
		stack.Stack.__init__(self)
		lexxer.Lexxer.__init__(self, file)
		#self.lexxer = shlex.shlex(instream=open(file, 'r'))
		self.source = 'include'
		self.debug = False 
		try:
			while 1:
				self.push(self.next())
		except StopIteration:
			pass

