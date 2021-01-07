'''
  Write a function that takes in an array of unique integers and returns its
  powerset.''' 
  
 Solution1 
 def powerset(array,idx = None): 
	if idx is None:
		idx = len(array) - 1 
	if idx < 0:
		return [[]] 
	ele = array[idx] 
	subsets = powerset(array,idx - 1) 
	for i in range(len(subsets)):
		currentSubset = subsets[i] 
		subsets.append(currentSubset + [ele]) 
	return subsets
