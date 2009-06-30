import os, sys, time
import excepts, scanner
import re

class Parser(scanner.Scanner):
	def __init__(self, file=False):
		if file == False or not os.path.isfile(file):
			raise excepts.InvalidArgs
		scanner.Scanner.__init__(self, file)
		self.keywords = (
			('if', self._if),			('elif', self._if), 		('while', self._wloop),
			('for', self._floop),		('include', self._inc),		(),
		)


	def _grok_type(self, item):
		return False

	def _cond(self, arg1=None, cond=None, arg2=None):
		if cond == None:
			raise excepts.InvalidArgs
		if type(arg1) != type(arg2):
			raise excepts.TypeMismatch
		if cond == '==': 
			if arg1 == arg2: return True
			else: return False
		elif cond == '!=':
			if arg1 != arg2: return True
			else: return False
		elif cond == '<':
			if arg1 < arg2: return True
			else: return False
		elif cond == '>':
			if arg1 > arg2: return True
			else: return False
		elif cond == '>=':
			if arg1 >= arg2: return True
			else: return False
		elif cond == '<=':
			if arg1 != arg2: return True
			else: return False

	def _if(self, arg1=None, cond=None, arg2=None):
		return self._cond(arg1, cond, arg2)

	def _wloop(self, arg1=None, cond=None, arg2=None):
		return self._cond(arg1, cond, arg2)
	
	def _floop(self, asgn=None, arg1=None,  cond=None, arg2=None, incr=None):
		return self._cond(arg1, cond, arg2)

	def _inc(self, file=None):
		return False

	# Rework this to use the keywords tuples
	# This method is going to get *FUCKING HUGE*
	def grok(self):
		while len(self.lang_stack) > 0:
			if self.lang_stack[0] == 'while': 
				if self.lang_stack[1] == '(' and self.lang_stack[5] == ')':
					self._wloop(self.lang_stack[2], self.lang_stack[3], self.lang_stack[4])
				elif self.lang_stack[1] == '(' and self.lang_stack[6] == ')' and self.lang_stack[5] != ')':
					self._wloop(self.lang_stack[2], self.lang_stack[3]+self.lang_stack[4], self.lang_stack[5])
			elif self.lang_stack[0] == 'if' or self.lang_stack[0] == 'elif':
				if self.lang_stack[1] == '(' and self.lang_stack[5] == ')':
					self._cond(self.lang_stack[2], self.lang_stack[3], self.lang_stack[4])
				elif self.lang_stack[1] == '(' and self.lang_stack[6] == ')' and self.lang_stack[5] != ')':
					self._cond(self.lang_stack[2], self.lang_stack[3]+self.lang_stack[4], self.lang_stack[5])
			self.pop(0)


