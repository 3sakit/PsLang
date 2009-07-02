import os, sys, time, re, types
import excepts, scanner, language

class Parser(scanner.Scanner, language.PsLang):
	def __init__(self, file=False, LibPath=None):
		if file == False or not os.path.isfile(file):
			raise excepts.InvalidArgs
		if LibPath == None:
			self.LibPath = ['./']
		else:
			if type(LibPath) != types.ListType and type(LibPath) != types.StringType:
				raise excepts.InvalidArgs, 'class Parser() given invalid args: LibPath must be a : seperated string, or a list of strings.'
			else:
				self.LibPath = LibPath
		scanner.Scanner.__init__(self, file, self.LibPath)
		language.PsLang.__init__(self, self.lang_stack)

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


