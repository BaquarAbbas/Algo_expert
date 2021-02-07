'''
  Write a function that takes in the head of a Singly Linked List, reverses the
  list in place (i.e., doesn't create a brand new list), and returns its new head.
'''

#Solution1 
def reverseLinkedList(head):
    cur = head 
	prev = None 
	while cur:
		nxt = cur.next 
		cur.next = prev 
		prev = cur
		cur = nxt 
	return prev
