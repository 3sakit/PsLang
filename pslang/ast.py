import pprint
import excepts

class Namespace:
	def __init__(self, name=None):
		if name == None:
			raise excepts.InvalidArgs, 'While instantiating a Namespace() object.'
		self.name = name
		self.children = []

	def new_child(self, name=None):
		return

class Ast:
	'''
	o = Ast()
	o.dump_namespace()
	o.new_parent('name')
	o.dump_namespace()
	'''
	def __init__(self):
		self.namespace = []

	def dump_namespace(self):
		pprint.pprint(self.namespace)

	def new_parent(self, name):
		return
