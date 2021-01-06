'''
  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.
  Note that the absolute difference of two integers is the distance between
  them on the real number line. For example, the absolute difference of -5 and 5
  is 10, and the absolute difference of -5 and -4 is 1.
'''

#Solution1
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")
	current  = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
	  elif firstNum > secondNum:
			current = firstNum - secondNum
			idxTwo += 1
		else:
			return [firstNum,secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum,secondNum]
	return smallestPair
  
  #Solution2
  def smallestDifference(arrayOne, arrayTwo):
    smallest = float("inf")
	current = float("inf")
	smallestPair = []
	for i in range(len(arrayOne)):
		for j in range(len(arrayTwo)):
			if arrayOne[i] < arrayTwo[j]:
				current = arrayTwo[j] - arrayOne[i]
			elif arrayOne[i] > arrayTwo[j]:
				current = arrayOne[i] - arrayTwo[j]
			else:
				return [arrayOne[i],arrayTwo[j]]
			if smallest > current:
				smallest = current
				smallestPair = [arrayOne[i],arrayTwo[j]]
	return smallestPair
