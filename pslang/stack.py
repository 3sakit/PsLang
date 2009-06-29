import excepts
import types

class Stack:
	''' '''
	def __init__(self):
		''' '''
		# This is our lang_stack
		self.lang_stack = []
		# Tweak this to adjust the number of past elements tracked
		self.max_last = 5
		self.last_stack = []
		# Don't tweak this
		self.current = None

	def push(self, item=False):
		''' '''
		if item == False:
			raise exceptions.InvalidArgs
		else:
			self.lang_stack.append(item)
			self.last_stack.append(item)
			while len(self.last_stack) > self.max_last:
				self.last_stack.pop(0)
	
	def pop(self, index=False):
		'''	'''
		if index == False:
			index = 0
		if type(index) != types.IntType:
			raise excepts.InvalidArgs
		self.lang_stack.pop(index)

