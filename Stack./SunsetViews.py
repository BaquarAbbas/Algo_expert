'''
  Given an array of buildings and a direction that all of the buildings face,
  return an array of the indices of the buildings that can see the sunset.
  
  A building can see the sunset if it's strictly taller than all of the
  buildings that come after it in the direction that it faces.
'''
#Solution1 
def sunsetViews(buildings, direction):
    buildingsWithSunsetViews = [] 
	
	startIdx = 0 if direction == 'WEST' else len(buildings) -1 
	step = 1 if direction == 'WEST' else -1 
	
	idx = startIdx 
	runningMaxHeight = 0 
	while idx >= 0 and idx < len(buildings):
		buildingHeight = buildings[idx] 
		
		if buildingHeight > runningMaxHeight:
			buildingsWithSunsetViews.append(idx) 
			
		runningMaxHeight = max(runningMaxHeight,buildingHeight)
		
		idx += step 
		
	if direction == "EAST":
		return buildingsWithSunsetViews[::-1] 
	
	return buildingsWithSunsetViews
  
#Solution2
def sunsetViews(buildings, direction):
    canditateBuildings = [] 
	
	startIdx = 0 if direction == 'EAST' else len(buildings) - 1
	step = 1 if direction == 'EAST' else -1 
	
	idx = startIdx 
	while idx >= 0 and idx < len(buildings):
		buildingHeight = buildings[idx] 
		
		while len(canditateBuildings) > 0 and buildings[canditateBuildings[-1]] <= buildingHeight:
			canditateBuildings.pop() 
			
		canditateBuildings.append(idx) 
		
		idx += step 
		
	if direction == 'WEST':
		return canditateBuildings[::-1] 
	
	return canditateBuildings 
  
'''buildings = [3, 5, 4, 4, 3, 1, 3, 2]
   direction = "EAST"
'''
