'''
  Write a function that takes in a Binary Tree (where nodes have an additional
  pointer to their parent node) as well as a node contained in that tree and
  returns the given node's successor.
  
  A node's successor is the next node to be visited (immediately after the given
  node) when traversing its tree using the in-order tree-traversal technique. A
  node has no successor if it's the last node to be visited in the in-order
  traversal.
  
  If a node has no successor, your function should return None/null.
'''

#Solution 
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
	inorderTraversalOrder = getInorderTraversalOrder(tree) 
	for idx,currentNode in enumerate(inorderTraversalOrder):
		if currentNode != node:
			continue
		if idx == len(inorderTraversalOrder) - 1:
			return None
		
		return inorderTraversalOrder[idx+1]
    
 def getInorderTraversalOrder(node,order = []):
	if node is None:
		return order 
	getInorderTraversalOrder(node.left) 
	order.append(node)
	getInorderTraversalOrder(node.right) 
	
	return order 
