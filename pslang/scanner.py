import shlex
import os
import excepts

class Stack:
	''' '''
	def __init__(self):
		''' '''
		# This is our stack
		self.stack = []
		# Tweak this to adjust the number of past elements tracked
		self.max_last = 5
		self.last = []
		# Don't tweak this
		self.current = None

	def push(self, item=False):
		''' '''
		if item == False:
			raise exceptions.InvalidArgs
		else:
			self.stack.append(item)
			self.last.append(item)
			while len(self.last) > self.max_last:
				self.last.pop(0)
	
	def pop(self, index=False):
		'''	'''
		stack_end = (len(self.last)-1)
		if index == False:
			self.last.pop(stack_end)
		else:
			self.stack.pop(index)
			if index <= self.max_last:
				self.last.pop(index)

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
