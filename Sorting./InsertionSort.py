'''
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Insertion Sort algorithm to sort the array.'''
  
  #Solution1 
  def insertionSort(array):
    for i in range(len(array)):
		j = i
		while j > 0 and array[j - 1] > array[j]:
			swap(array,j,j-1)
			j = j - 1
	return array
def swap(array,i,j):
	array[i],array[j] = array[j],array[i]
'''array = [8, 5, 2, 9, 5, 6, 3]'''
