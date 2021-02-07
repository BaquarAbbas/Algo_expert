'''
  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing only 0s and 1s.Each 0s represents part of a river. 
  A river consists of any number of 1s that are either horizontally or vertically adjacent 
  (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.
  Note that a river can twist. In other words, it doesn't have to be a straight
  vertical line or a straight horizontal line; it can be L-shaped, for example.
  Write a function that returns an array of the sizes of all rivers represented
  in the input matrix. The sizes don't need to be in any particular order.
'''
#Solution1 
def riverSizes(matrix):
	sizes = []
	visited = [[False for value in row] for row in matrix] 
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j]:
				continue 
			traverseNode(i,j,matrix,visited,sizes) 
	return sizes 

def traverseNode(i,j,matrix,visited,sizes):
	currentRiverSize = 0 
	nodesToExplore = [[i,j]]
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop() 
		i = currentNode[0] 
		j = currentNode[1] 
		if visited[i][j]:
			continue 
		visited[i][j] = True 
		if matrix[i][j] == 0:
			continue 
		currentRiverSize += 1
		unvisitedNeighbours = getUnvisitedNodes(i,j,matrix,visited) 
		for neighbor in unvisitedNeighbours:
			nodesToExplore.append(neighbor) 
	if currentRiverSize > 0:
		sizes.append(currentRiverSize) 
    
def getUnvisitedNodes(i,j,matrix,visited):
	unvisitedNeighbors = [] 
	if i > 0 and not visited[i -1][j]:
		unvisitedNeighbors.append([i-1,j]) 
	if i < len(matrix) - 1 and not visited[i+1][j]:
		unvisitedNeighbors.append([i+1,j]) 
	if j > 0 and not visited[i][j-1]:
		unvisitedNeighbors.append([i,j-1]) 
	if j < len(matrix[0]) - 1 and not visited[i][j+1]:
		unvisitedNeighbors.append([i,j+1]) 
	return unvisitedNeighbors
  
  '''matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]'''
    
