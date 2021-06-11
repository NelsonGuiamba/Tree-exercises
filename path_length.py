import  sys
#help(path)
sys.path.append('./ch08')
from linked_binary_tree import LinkedBinaryTree as	Arvore
def path_len(T,p=None,d=0):
	def recur(T,p,d):
		
		if T.num_children(p) == 0:
			return d
		else:
			if T.left(p) != None:
				a = recur(T,T.left(p),d+1)
			else: a = 0
			if T.right(p) != None:
				b = recur(T,T.right(p),d+1)
			else:b = 0
			#print(f'No: {p._node._element} : {a} + {b} ={a+b}')
			return d+a+b
	if p != None:
		if d == 0 and p != T.root():
			raise ValueError('d is not 0 and p is not root')
		return recur(T,p,0)
	else:
		return recur(T,T.root(),d)
def preorder_indent(T, p, d):
  """Print preorder representation of subtree of T rooted at p at depth d."""
  print(2*d*' ' + str(p.element()))           # use depth for indentation
  for c in T.children(p):
    preorder_indent(T, c, d+1)   
if __name__ == '__main__':
	a = Arvore()
	a._add_root(2)
	#print(path_len(a))
	l = a._add_left(a.root(),3)
	r = a._add_right(a.root(),4)
	#print(path_len(a))
	#print(path_len(a))
	r = a._add_left(r,5)
	a._add_right(r,8)
	print('path',path_len(a))
	preorder_indent(a,a.root(),0)
	
	