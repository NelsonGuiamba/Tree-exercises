import  sys
#help(path)
sys.path.append('./ch08')
from linked_binary_tree import LinkedBinaryTree as	Arvore
class ExpressionTree(Arvore):
	def __init__(self,t,l=None,r=None):
		super().__init__()
		if not isinstance(t, str):
			raise TypeError( 'Token must be a string ')
		self._add_root(t)
		if l is not None:
			 if t not in '+-*x/' :
			 	raise ValueError( 'token must be valid operator ')
			 self._attach(self.root(), l, r)
	def evaluate(self,d):
		return self._evaluate_recur(self.root(),d)
	
	def _evaluate_recur(self,p,d):
		if self.is_leaf(p):
			print(p.element())
			return float(d[p.element()])
		else:
			op = p.element()
			left = self._evaluate_recur(self.left(p),d)
			right = self._evaluate_recur(self.right(p),d)
			if op == '+':return left+right
			elif op == '-':return left-right
			elif op == '*':return left*right
			else:return left/right
	def toPosfix(self):
		a = ''
		for i in self.postorder():
			if i.element() in '+/-*x':
				a += i.element() +' '
			else:
				a +=  i.element()
		return a
def build(tokens):
	S = []
	for t in tokens:
		if t in '+-x*/' : S.append(t)
		elif t not in '()':S.append(ExpressionTree(t))
		elif t== ')' :
			right = S.pop( )
			op = S.pop( )
			left = S.pop( )
			S.append(ExpressionTree(op, left, right)) # repush tree # we ignore a left parenthesis return 
	return S.pop()
def preorder_indent(T, p, d):
  """Print preorder representation of subtree of T rooted at p at depth d."""
  print(2*d*' ' + str(p.element()))           # use depth for indentation
  for c in T.children(p):
    preorder_indent(T, c, d+1)  
if __name__ == '__main__':
	t = build('((a+b)/(b*a))')
	preorder_indent(t,t.root(),0)
	print(t.evaluate({'a':3,'b':5}))
	print(t.toPosfix())