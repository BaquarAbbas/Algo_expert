'''
  Write a function that takes in the head of a Singly Linked List and an integer k
  and removes the kth node from the end of the list.
  The removal should be done in place, meaning that the original data structure
  should be mutated (no new structure should be created).
  '''
#Solution1
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def removeKthNodeFromEnd(head, k):
    # Write your code here.
    first  = head 
	second = head 
	counter = 1 
	while counter <=k:
		counter += 1 
		second = second.next 
	if second is None:
		head.value = head.next.value 
		head.next = head.next.next 
		return 
	while second.next is not None:
		second = second.next 
		first = first.next 
	first.next = first.next.next 
