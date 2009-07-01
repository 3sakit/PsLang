import shlex
import os, sys, time
import excepts

class Lexxer(shlex.shlex):
	def __init__(self, fname=None):
		if fname == None:
			raise excepts.InvalidArgs, 'Class Lexxer() given invalid arguments at instantiation.'
		shlex.shlex.__init__(self, open(fname, 'r'), fname)

	def sourcehook(self, newfile):
		"Hook called on a filename to be sourced."
		if newfile[0] == '"':
			newfile = newfile[1:-1]
		# This implements cpp-like semantics for relative-path inclusion.
		if isinstance(self.infile, basestring) and not os.path.isabs(newfile):
			#newfile = os.path.join(os.path.dirname(self.infile), newfile)
			newfile = '/root/git/pslang/examples/'+newfile+'.psl'
		return (newfile, open(newfile, "r"))
	
