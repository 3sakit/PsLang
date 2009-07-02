import shlex, types
import os, sys, time
import excepts

class Lexxer(shlex.shlex):
	def __init__(self, fname=None, LibPath=None):
		if fname == None or os.path.isfile(fname) == False:
			raise excepts.InvalidArgs, 'Class Lexxer() given invalid arguments: fname must be a valid path+filename.'
		if type(LibPath) != types.ListType and type(LibPath) != types.StringType:
			raise excepts.InvalidArgs, 'Class Lexxer() given invalid arguments: LibPath must be a ListType or StringType.'
		elif LibPath == None:
			self.LibPath = ['./']
		else:
			if type(LibPath) == types.ListType:
				self.LibPath = LibPath
			elif type(LibPath) == types.StringType:
				if LibPath.find(':') == -1 and len(shlex.split(LibPath)) > 1:
					raise excepts.InvalidArgs, 'Class Lexxer() given invalid arguments: ListType when a string must have \':\' seperated fields.'
				elif LibPath.find(':') == -1 and len(shlex.split(LibPath)) < 2:
					self.LibPath = [LibPath]
				elif LibPath.find(':') != -1:
					self.LibPath = LibPath.split(':')
				else:
					self.LibPath = [LibPath] # and hope for the best
		shlex.shlex.__init__(self, open(fname, 'r'), fname)

	def sourcehook(self, newfile):
		"Hook called on a filename to be sourced."
		if newfile[0] == '"':
			newfile = newfile[1:-1]
		# This implements cpp-like semantics for relative-path inclusion.
		if isinstance(self.infile, basestring) and not os.path.isabs(newfile):
			for path in self.LibPath:
				if os.path.isfile(path+newfile+'.psl'):
					newfile = path+newfile+'.psl'
					print 'Sourcing: '+newfile
					break
		return (newfile, open(newfile, "r"))
	
