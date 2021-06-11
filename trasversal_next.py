import  sys
#help(path)
sys.path.append('/storage/emulated/0/python/Goodrich/ch08')
from linked_binary_tree import LinkedBinaryTree as	Arvore
def preorder_next(T,p):
	if T.num_children(p) == 0:
		#print('in')
		pai = T.parent(p)
		while pai != T.root():
			if T.left(pai) == p:
				return T.right()
			pai =  T.parent(pai)
		#print('Cond',pai==T.root())
		return T.right(pai)
	else:
		if T.left(p) != None:
			return T.left(p)
		if T.right(p) != None:
			return T.right(p)

def postorder_next(T,p,est=False):
	#print(p.element(),est)
	if est == False:
		if p == T.root():
			if T.left(p) != None:
				return postorder_next(T,T.left(p),True)
			if T.right(p) != None:
				return postorder_next(T,T.right(p),True)
			return p 
		pai = T.parent(p)
		if T.left(pai) == p:
			if T.right(pai) != None:
				return postorder_next(T,T.right(pai),True)
			else:
				return T.parent(p)
		if T.right(pai) == p:
			return T.parent(pai)
	else:
		if T.num_children(p) != 0:
			if T.left(p) != None:
				return postorder_next(T,T.left(p),est)
			if T.right(p) != None:
				return postorder_next(T,T.right(p),est)
		else:
			#print('end')
			return p
def preorder_indent(T, p, d):
  """Print preorder representation of subtree of T rooted at p at depth d."""
  print(2*d*' ' + str(p.element()))           # use depth for indentation
  for c in T.children(p):
    preorder_indent(T, c, d+1)  
if  __name__ == '__main__' :
	a = Arvore()
	a._add_root(1)
	a._add_right(a.root(),90)
	l = a._add_left(a.root(),2)
	r = a._add_right(l,3)
	a._add_left(r,89)
	llg = a._add_left(l,5)
	rr = a._add_right(r,4)
	rr=a._add_right(rr,44)
	preorder_indent(a,a.root(),0)
	print(a.root().element(),' Result',postorder_next(a,a.root()).element())