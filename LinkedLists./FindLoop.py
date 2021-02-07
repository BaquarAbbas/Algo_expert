'''
  Write a function that takes in the head of a Singly Linked List that contains
  a loop (in other words, the list's tail node points to some node in the list
  instead of None/null.The function should returnthe node (the actual node--not just its value) 
  from which the loop originates in constant space.
  '''
  
 #Solution1
 class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def findLoop(head):
    p = head.next 
	q = head.next.next 
	while p != q:
		p = p.next 
		q = q.next.next 
	p = head
	while p != q:
		p = p.next 
		q = q.next 
	return p
