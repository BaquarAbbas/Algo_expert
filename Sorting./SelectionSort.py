'''
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Selection Sort algorithm to sort the array.
'''
#Solution1 
def selectionSort(array):
	current_idx = 0
	while current_idx < len(array) - 1:
		smallest_idx = current_idx
		for i in range(current_idx+1,len(array)):
			if array[smallest_idx] > array[i]:
				smallest_idx = i
		swap(array,current_idx,smallest_idx)
		current_idx += 1
	return array
def swap(array,i,j):
	array[i],array[j] = array[j],array[i]
		
#Solution2 
def selectionSort(array):
    for i in range(len(array)-1):
		index = i
		for j in range(i+1,len(array),1):
			if array[j] < array[index]:
				index = j
		if index != i:
			swap(array,index,i)
	return array
def swap(array,i,j):
	array[i],array[j] = array[j],array[i]
  
'''array = [8, 5, 2, 9, 5, 6, 3]''' 
