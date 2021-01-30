'''
  You're given an integer start and a list edges of pair of integers.
  The list is what's called an adjacency list, and it represents a graph. The
  number of vertices in the graph is equal to the length of edges ,where each index i in edges  contains vertex i's's outbound edges, 
  in no particular order. Each individual edge is represented by an pair of two numbers [destination, distance].
  
  Write a function that computes the lengths of the shortest paths between start and all of the other vertices in the graph using Dijkstra's
  algorithm and returns them in an array. Each index i in the output array should represent the length of the shortest path between start and vertex
  i . If no path is found from start to vertex i then output[i] should be -1.Note that the graph represented by edges won't contain any self-loops.
  '''
  #solution1 
  def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges) 
	
	minDistances = [float('inf') for _ in range(numberOfVertices)] 
	minDistances[start] = 0 
	
	visited = set()
	
	while len(visited) != numberOfVertices:
		vertex,currentMinDistance = getVertexWithMinDistance(minDistances,visited) 
		
		if currentMinDistance == float('inf'):
			break
			
		visited.add(vertex) 
		
		for edge in edges[vertex]:
			destination,distanceToDestination = edge 
			
			if destination in visited:
				continue 
				
			newPathDistance = currentMinDistance + distanceToDestination 
			currentDestinationDistance = minDistances[destination] 
			if newPathDistance < currentDestinationDistance:
				minDistances[destination] = newPathDistance 
				
	return list(map(lambda x: -1 if x == float('inf') else x,minDistances))
  
 def getVertexWithMinDistance(distances,visited):
	currentMinDistance = float('inf') 
	vertex = -1 
	
	for vertexIdx,distance in enumerate(distances):
		if vertexIdx in visited:
			continue 
		if distance <= currentMinDistance:
			vertex = vertexIdx 
			currentMinDistance = distance 
			
	return vertex,currentMinDistance 
  
  '''start = 0 
  edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]'''
