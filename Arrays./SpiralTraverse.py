'''Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in spiral order.
  Spiral order starts at the top left corner of the two-dimensional array, goes
  to the right, and proceeds in a spiral pattern all the way until every element
  has been visited.'''
  #Solution1 
  def spiralTraverse(array):
    result = [] 
    startRow,endRow = 0,len(array)-1 
    startCol,endCol = 0,len(array[0]) - 1 
    
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol,endCol+1):
            result.append(array[startRow][col]) 
        for row in range(startRow +1,endRow+1):
            result.append(array[row][endCol]) 
        for col in reversed(range(startCol,endCol)):
            if startRow == endRow:
                break 
            result.append(array[endRow][col]) 
        for row in reversed(range(startRow+1,endRow)):
            if startCol == endCol:
                break 
            result.append(array[row][startCol])
        startRow += 1 
        endRow -= 1
        startCol += 1 
        endCol -= 1 
    return result 
    
    #Solution2 
    def spiralTraverse(array):
    result = [] 
	spiralFill(array,0,len(array) -1,0,len(array[0]) -1,result)
	return result 

def spiralFill(array,startRow,endRow,startCol,endCol,result):
	if startRow > endRow or startCol > endCol:
		return 
	for col in range(startCol,endCol+1):
		result.append(array[startRow][col])
		
	for row in range(startRow +1,endRow +1):
		result.append(array[row][endCol]) 
		
	for col in reversed(range(startCol,endCol)):
		if startRow == endRow:
			break 
		result.append(array[endRow][col]) 
		
	for row in reversed(range(startRow+1,endRow)):
		if startCol == endCol:
			break
		result.append(array[row][startCol])
	
	spiralFill(array,startRow + 1,endRow - 1,startCol + 1,endCol - 1,result)
