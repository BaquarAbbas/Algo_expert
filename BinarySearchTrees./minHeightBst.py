'''
  Write a function that takes in a non-empty sorted array of distinct integers,
  constructs a BST from the integers, and returns the root of the BST.
'''
#Solution1
def minHeightBst(array):
    return constructMinHeight(array, None, 0, len(array)-1)

def constructMinHeight(array, bst, startIdx, endIdx):
	if endIdx < startIdx:
		return
	midIdx = (startIdx + endIdx)//2 
	valueToAdd = array[midIdx] 
	if bst is None:
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd) 
	constructMinHeight(array,bst,startIdx,midIdx - 1)
	constructMinHeight(array,bst,midIdx +1,endIdx)
	return bst 
	


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
                
#Solution2 
def minHeightBst(array):
    return constructMinHeight(array,0,len(array)-1)

def constructMinHeight(array, startIdx, endIdx):
	if endIdx < startIdx:
		return None 
	midIdx = (startIdx + endIdx) // 2
	bst = BST(array[midIdx]) 
	bst.left = constructMinHeight(array,startIdx,midIdx -1) 
    bst.right = constructMinHeight(array,midIdx + 1,endIdx)
	return bst 


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
