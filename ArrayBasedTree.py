import sys
sys.path.append('./ch08')
from binary_tree import BinaryTree as bTree

class ArrayBinaryTree(bTree):
	class _Position(bTree.Position):
		def __init__(self,container,node):
			self._container = container
			self._node = node
		
		def element(self):
			return self._node._element
		
		
	class _Node:
		def __init__(self,i,element,parent=None,left=None,right=None):
			self._index = i
			self._element = element
			self._parent  = parent
			self._left = left
			self._right = right
		
		def element(self):
			return self._element
		
		def __eq__(self, other):
			return type(other) is type(self) and other._node is self._node
	def _validate(self,p):
	    if not isinstance(p, self.Position):
	    	raise TypeError('p must be proper Position type')
	    if p._container is not self:
	    	raise ValueError('p does not belong to this container')
	    if p._node._parent is p._node:
	    	raise ValueError('p is no longer valid')
	    return p._node
	def _make_position(self, node):
		return self._Position(self, node) if node is not None else None
	
	def __init__(self):
		self._data = [None]
	
	def root(self):
		if self._data[0] == None:raise ValueError('Root does not exits')
		return self._make_position(self._data[0])
	
	def left(self,p):
		p = self._validate(p)
		return self._make_position(p._left)
	
	def right(self,p):
		p = self._validate(p)
		return self._make_position(p._right)
	
	def parent(self,p):
		p = self._validate(p)
		return self._make_position(p._parent)
	
	def _add_root(self,e):
		if self._data[0] != None:
			raise ValueError('root exits')
		self._resize()
		self._data[0] = self._Node(0,e)
		return self._make_position(self._data[0])
	def _add_left(self,p,e):
		p = self._validate(p)
		if p._left != None:
			raise ValueError('left child exits')
		i = 2*p._index + 1
		self._resize(i)
		self._data[i] = self._Node(i,e,p)
		p._left = self._data[i]
		return self._make_position(self._data[i])
	def _add_right(self,p,e):
		p = self._validate(p)
		if p._right != None:
			raise ValueError('left child exits')
		i = 2*p._index + 2
		self._resize(len(self._data)*2+1)
		self._data[i] = self._Node(i,e,p)
		p._right = self._data[i]
		return self._make_position(self._data[i])
	def _resize(self,n=None):
		if n == None: n = len(self._data) *2
		d = [None]*len(self._data)
		for i in range(len(self._data)):
			d[i] = self._data[i]
		for _ in range(n-i):
			d.append(None)
		self._data = d
def preorder_indent(T, p, d):
  """Print preorder representation of subtree of T rooted at p at depth d."""
  print(2*d*' ' + str(p.element()))           # use depth for indentation
  for c in T.children(p):
    preorder_indent(T, c, d+1)
if __name__ == '__main__':
	a = ArrayBinaryTree()
	r = a._add_root(6)
	#a._add_right(r,12)
	r = a._add_left(r,8)
	a._add_right(r,14)
	a._add_left(r,10)
	preorder_indent(a,a.root(),0)
	