import shlex
import os
import exceptions

class Stack:
	'''
	'''
	def __init__(self):
		'''
		'''
		# This is our stack
		self.stack = []
		# Tweak this to adjust the number of past elements tracked
		self.max_last = 5
		self.last = []
		# Tweak this to adjust the number of future elements tracked
		self.max_next = 5
		self.next = []
		# Don't tweak this
		self.current = None

	def __push_last(self, item=None):

	def push(self, item=None, index=None):


class Scanner:
	'''
	'''
	def __init__(self, file=None):
		'''
		'''
		if file == None:
			raise exceptions.InvalidArgs
		self.file = open(file, 'r')

