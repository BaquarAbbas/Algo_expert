'''
  Write a function that takes in the heads of two Singly Linked Lists that are
  in sorted order, respectively. The function should merge the lists in place
  (i.e., it shouldn't create a brand new list) and return the head of the merged
  list; the merged list should be in sorted order.
  
  Each LinkedList has an integer value as well as next node pointing to nextnode in
  the list;in other words,the heads will never be NULL/None.
'''
#Solution1
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
 def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    p = headOne 
	q = headTwo 
	s = None 
	if not p:
		return q
	if not q:
		return p 
	if p and q:
		if p.value <= q.value:
			s = p 
			p = p.next 
		else:
			s = q 
			q = q.next 
	    new_head = s 
	while p and q:
		if p.value <= q.value:
			s.next = p 
			s = p 
			p = p.next 
		else:
			s.next = q 
			s = q 
			q = q.next 
	if not p:
		s.next = q 
	if not q:
		s.next = p 
	return new_head

'''headOne = 2->6->7->8
   headTwo = 1->3->4->5->9->10
'''
