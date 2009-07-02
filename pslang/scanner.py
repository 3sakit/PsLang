import lexxer, stack 
import os

class Scanner(lexxer.Lexxer, stack.Stack):
	'''	'''
	def __init__(self, file=None, LibPath=None):
		'''	'''
		if file == None:
			raise exceptions.InvalidArgs
		self.LibPath = LibPath
		stack.Stack.__init__(self)
		lexxer.Lexxer.__init__(self, file, self.LibPath)
		#self.lexxer = shlex.shlex(instream=open(file, 'r'))
		self.source = 'include'
		self.debug = False 
		try:
			while 1:
				self.push(self.next())
		except StopIteration:
			pass

