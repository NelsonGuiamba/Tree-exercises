import  sys
#help(path)
sys.path.append('./ch08')
from linked_binary_tree import LinkedBinaryTree as	Arvore
def preorder_indent(T, p, d):
  """Print preorder representation of subtree of T rooted at p at depth d."""
  print(2*d*' ' + str(p.element()))           # use depth for indentation
  for c in T.children(p):
    preorder_indent(T, c, d+1)     
def lcd(T,p,q):
	if p == T.root() or T.root() == q:
		return T.root()
	d1 = T.depth(p)
	d2 = T.depth(q)
	if d1 == d2:
		pai = T.parent(p)
		if T.left(pai) == p and  T.right(pai) == q:
			return pai
		if T.right(pai) == p and T.left(pai) == q:
			return pai
	elif d1 < d2:
		return lcd(T,p,T.parent(q))
	else:
		return lcd(T,T.parent(p),q)
if __name__ == '__main__':
	a = Arvore()
	r = a._add_root(1)
	l = a._add_left(r,2)
	a._add_left(l,4)
	a._add_right(l,5)
	r = a._add_right(r,3)
	l = a._add_left(r,6)
	r = a._add_right(r,7)
	a._add_left(r,8)
	r = a._add_right(r,9)
	preorder_indent(a,a.root(),0)
	print(r.element(),l.element(),lcd(a,r,l).element())