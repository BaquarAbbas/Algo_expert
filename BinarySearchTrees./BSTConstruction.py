'''
  Write a  class for a Binary Search Tree. The class should
  support:
  - Inserting values with the insert method. 
  - Removing values with the remove method.this method should
    only remove the first instance of a given value.
  - Searching for values with the contains method.
'''
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
        return self

    def contains(self, value):
        if value < self.value:
			if self.left is None:
				return False 
			else:
				return self.left.contains(value) 
		elif value > self.value:
			if self.right is None:
				return False 
			else:
				return self.right.contains(value) 
		else:
			return True 

    def remove(self, value,parent = None):
        if value < self.value:
			if self.left is not None:
				self.left.remove(value,self)
		elif value > self.value:
			if self.right is not None:
				self.right.remove(value,self)
		else:
			if self.left is not None and self.right is not None:
				self.value = self.right.getMinvalue() 
				self.right.remove(self.value,self) 
			elif parent is None:
				if self.left is not None:
					self.value = self.left.value 
					self.right = self.left.right 
					self.left  = self.left.left
				elif self.right is not None:
					self.value = self.right.value 
					self.right = self.right.right 
					self.left = self.right.left
			
			elif parent.left == self:
				parent.left = self.left if self.left is not None else self.right 
			elif parent.right == self:
				parent.right = self.right if self.right is not None else self.left
			else:
				#do nothing 
				pass 
        return self
	def getMinvalue(self):
		if self.left is None:
			return self.value 
		else:
			return self.left.getMinvalue()
