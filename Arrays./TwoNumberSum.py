#solution1
def twoNumberSum(array, targetSum):
    for i in range(len(array) -1):
	    firstNum = array[i]
		for j in range(i + 1,len(array)):
		    secondNum = array[j]
			if firstNum + secondNum == targetSum:
			    return [firstNum,secondNum]
    return []

   
 #solution2
 def twoNumberSum(array, targetSum):
    nums ={}
    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            return [potential_match,num]
        else:
             nums[num] = True
            
    return []
#solution3   
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	while left < right:
		currentsum = array[left] + array[right]
		if currentsum == targetSum:
		    return [ array[left], array[right]]
		elif currentsum < targetSum:
			left += 1
		elif currentsum > targetSum:
			right -= 1		
	return []

 '''array = [3, 5, -4, 8, 11, 1, -1, 6]
 targetSum = 10 '''
    
