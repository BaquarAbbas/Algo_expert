'''
  You're given the head of a Singly Linked List whose nodes are in sorted order
  with respect to their values. Write a function that returns a modified version
  of the Linked List that doesn't contain any nodes with duplicate values. The
  Linked List should be modified in place (i.e., you shouldn't create a brand
  new list), and the modified Linked List should still have its nodes sorted
  with respect to their values.
'''
#Solution1 
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def removeDuplicatesFromLinkedList(linkedList):
    cur  = linkedList
	prev = None
	duplicates = dict()
	while cur is not None:
		if cur.value in duplicates:
			prev.next = cur.next
			cur = prev
		else:
			duplicates[cur.value] = 1
			prev = cur 
		cur = cur.next
	return linkedList
  
 #Solution2 
 def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    currentNode = linkedList
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
			nextDistinctNode = nextDistinctNode.next 
			
		currentNode.next = nextDistinctNode
		currentNode = nextDistinctNode
	return linkedList#This solution is having the same class of LinkedList that is implemented above
  
  '''linkedList = 1->1->3->4->4->4->5->6->6'''
