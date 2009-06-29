import os, sys, time
import excepts, scanner

class Parser(scanner.Scanner):
	def __init__(self, file=False):
		if file == False or not os.path.isfile(file):
			raise excepts.InvalidArgs
		scanner.Scanner.__init__(self, file)

	def _cond(self, arg1=None, cond=None, arg2=None):
		if cond == None:
			raise excepts.InvalidArgs
		if cond == '==': 
			if arg1 == arg2: 
				print '('+str(arg1)+' == '+str(arg2)+') = True'
				return True
			else: 
				print '('+str(arg1)+' == '+str(arg2)+') = False'
				return False
		elif cond == '!=':
			if arg1 != arg2: 
				print '('+str(arg1)+' != '+str(arg2)+') = True'
				return True
			else: 
				print '('+str(arg1)+' != '+str(arg2)+') = False'
				return False
		elif cond == '<':
			if arg1 < arg2: 
				print '('+str(arg1)+' < '+str(arg2)+') = True'
				return True
			else: 
				print '('+str(arg1)+' < '+str(arg2)+') = False'
				return False

		elif cond == '>':
			if arg1 > arg2: 
				print '('+str(arg1)+' > '+str(arg2)+') = True'
				return True
			else: 
				print '('+str(arg1)+' > '+str(arg2)+') = False'
				return False
		elif cond == '>=':
			if arg1 >= arg2: 
				print '('+str(arg1)+' >= '+str(arg2)+') = True'
				return True
			else: 
				print '('+str(arg1)+' >= '+str(arg2)+') = False'
				return False
		elif cond == '<=':
			if arg1 != arg2: 
				print '('+str(arg1)+' <= '+str(arg2)+') = True'
				return True
			else: 
				print '('+str(arg1)+' <= '+str(arg2)+') = False'
				return False

	def _wloop(self, arg1=None, cond=None, arg2=None):
		sys.stdout.write('while ')
		self._cond(arg1, cond, arg2)

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

if __name__ == '__main__':
	print 'Parsing '+sys.argv[1]
	o = Parser(sys.argv[1])
	o.grok()
	print dir(o)
	print o.lang_stack
