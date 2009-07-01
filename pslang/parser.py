import os, sys, time, re, types
import excepts, scanner, language

class Parser(scanner.Scanner, language.PsLang):
	def __init__(self, file=False):
		if file == False or not os.path.isfile(file):
			raise excepts.InvalidArgs
		scanner.Scanner.__init__(self, file)
		language.PsLang.__init__(self, self.lang_stack)

	def _inc(self, file=None):
		fname = '/root/git/pslang/examples/'+self.lang_stack[(self.tkn_pos+1)]+'.psl'
		print 'Including file: '+fname
		spec = self.sourcehook(fname)
		if spec:
			(nfile, nstream) = spec
			self.push_source(nstream, nfile)
		else:
			print 'booboo'
		return True

	# Rework this to use the keywords tuples
	# This method is going to get *FUCKING HUGE*
	def grok(self):
		self.tkn_pos = 0
		while self.tkn_pos < len(self.lang_stack):
			for kword in self.keywords:
				if self.lang_stack[self.tkn_pos] == kword[0]:
					kword[1]()
	#		for kword in self.namespace:
			self.tkn_pos += 1


