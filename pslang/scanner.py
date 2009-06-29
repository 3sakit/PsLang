import shlex
import os

class Scanner:
	'''	'''
	def __init__(self, file=None):
		'''	'''
		if file == None:
			raise exceptions.InvalidArgs
		self.lexxer = shlex.shlex(instream=open(file, 'r'))
		self.stack = Stack()
		try:
			while 1:
				self.stack.push(self.lexxer.next())
		except StopIteration:
			pass

try:
	import sys
	o = Scanner(file=sys.argv[1])
	print dir(o)
	print o.stack.stack
	print o.stack.last
except:
	pass
