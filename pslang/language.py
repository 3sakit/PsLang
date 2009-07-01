import os, sys, time
import excepts, scanner
import re, types

class PsLang:
	def __init__(self, stack=None):
		if stack == None: 
			raise excepts.InvalidArgs, 'Bad value for <stack> during PsLang() init.'
		self.psl_stack = stack
		self.keywords = (
			('if', self._if),			('elif', self._if), 		('else', self._if),
			('while', self._wloop),		('for', self._floop),		('include', self._inc)
		)
		self.namespace = [
			('print', self._print), ('exec', self._exec)
		]

	def _print(self, msg=None):
		print msg

	def _exec(self, cmd=None):
		print 'exec %s' % cmd

	def _cond(self, arg1=None, cond='==', arg2=None):
		if cond == None:
			cond = '=='
			#raise excepts.InvalidArgs
		
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
		if arg1 == None:
			arg1 = self.lang_stack[(self.tkn_pos+2)]
		if cond == None:
			for t_cnd in ('==', '!=', '<=', '>='):
				if self.lang_stack[(self.tkn_pos+3)]+self.lang_stack[(self.tkn_pos+4)] == t_cnd:
					cond = self.lang_stack[(self.tkn_pos+3)]+self.lang_stack[(self.tkn_pos+4)]
					arg2 = self.lang_stack[(self.tkn_pos+5)]
		if cond == None:
			for t_cnd in ('<', '>'):
				if self.lang_stack[(self.tkn_pos+3)] == t_cnd:
					cond = self.lang_stack[(self.tkn_pos+3)]
					arg2 = self.lang_stack[(self.tkn_pos+4)]

		print '%s (%s %s %s) { ... }' % (self.lang_stack[self.tkn_pos], arg1, cond, arg2)
		return self._cond(arg1, cond, arg2)

	def _wloop(self, arg1=None, cond=None, arg2=None):
		if arg1 == None:
			arg1 = self.lang_stack[(self.tkn_pos+2)]
		if cond == None:
			for t_cnd in ('==', '!=', '<=', '>='):
				if self.lang_stack[(self.tkn_pos+3)]+self.lang_stack[(self.tkn_pos+4)] == t_cnd:
					cond = self.lang_stack[(self.tkn_pos+3)]+self.lang_stack[(self.tkn_pos+4)]
					arg2 = self.lang_stack[(self.tkn_pos+5)]
		if cond == None:
			for t_cnd in ('<', '>'):
				if self.lang_stack[(self.tkn_pos+3)] == t_cnd:
					cond = self.lang_stack[(self.tkn_pos+3)]
					arg2 = self.lang_stack[(self.tkn_pos+4)]

		print 'while (%s %s %s) { ... }' % (arg1, cond, arg2)
		return self._cond(arg1, cond, arg2)
	
	def _floop(self, asgn=None, arg1=None,  cond=None, arg2=None, incr=None):
		if asgn == None:
			asgn = self.lang_stack[(self.tkn_pos+2)]
			aval = self.lang_stack[(self.tkn_pos+4)]
		if arg1 == None:
			arg1 = self.lang_stack[(self.tkn_pos+6)]
		if cond == None:
			for t_cnd in ('==', '!=', '<=', '>='):
				if self.lang_stack[(self.tkn_pos+7)]+self.lang_stack[(self.tkn_pos+8)] == t_cnd:
					cond = self.lang_stack[(self.tkn_pos+7)]+self.lang_stack[(self.tkn_pos+8)]
					arg2 = self.lang_stack[(self.tkn_pos+9)]
					if incr == None:
						incr = self.lang_stack[(self.tkn_pos+11)]
						t_ch = self.lang_stack[(self.tkn_pos+12)]+self.lang_stack[(self.tkn_pos+13)]
						if t_ch != '++' and t_ch != '--' and t_ch != '**':
							raise excepts.SyntaxError, 'B Stack position: '+str(self.tkn_pos)+' '+t_ch
						else:
							t = incr+t_ch
						incr = t

		if cond == None:
			for t_cnd in ('<', '>'):
				if self.lang_stack[(self.tkn_pos+7)] == t_cnd:
					cond = self.lang_stack[(self.tkn_pos+7)]
					arg2 = self.lang_stack[(self.tkn_pos+8)]
					if incr == None:
						incr = self.lang_stack[(self.tkn_pos+10)]
						t_ch = self.lang_stack[(self.tkn_pos+11)]+self.lang_stack[(self.tkn_pos+12)]
						if t_ch != '++' and t_ch != '--' and t_ch != '**':
							raise excepts.SyntaxError, 'S Stack position: '+str(self.tkn_pos)+' '+t_ch
						else:
							t = incr+t_ch
						incr = t

		print 'for (%s=%s; %s %s %s; %s) { ... }' % (asgn, aval, arg1, cond, arg2, incr)
		return self._cond(arg1, cond, arg2)

