'''
  Write a function that takes in a potentially invalid Binary Search Tree (BST)
  and returns a boolean representing whether the BST is valid.
'''
#Solution1 
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	return validateBSTHelper(tree,float("-inf"),float("inf"))
		
def validateBSTHelper(tree,minValue,maxValue):
	if tree is None:
		return True 
	if tree.value < minValue or tree.value >= maxValue:
		return False
	leftIsValid = validateBSTHelper(tree.left,minValue,tree.value)
	return leftIsValid and validateBSTHelper(tree.right,tree.value,maxValue)
  
'''tree =10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
'''
