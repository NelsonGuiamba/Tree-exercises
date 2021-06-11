import  sys
#help(path)
sys.path.append('./ch08')
from linked_binary_tree import LinkedBinaryTree as	Arvore
def preorder(T):
	def pre(T,p,l):
		for c in T.children(p):
			l.append(c.element())
			pre(T,c,l)
	l = [T.root().element()]
	pre(T,T.root(),l)
	return l
def preorder_indent(T, p, d):
  """Print preorder representation of subtree of T rooted at p at depth d."""
  print(2*d*' ' + str(p.element()))           # use depth for indentation
  for c in T.children(p):
    preorder_indent(T, c, d+1)
if __name__ == '__main__':
	a = Arvore()
	r = a._add_root(3)
	l = a._add_left(r,4)
	a._add_left(l,10)
	r = a._add_right(r,5)
	l = a._add_left(r,6)
	a._add_left(l,9)
	r = a._add_right(r,7)
	preorder_indent(a,a.root(),0)
	print(preorder(a))