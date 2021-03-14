'''
  You're given a list of arbitrary jobs that need to be completed; these jobs
  are represented by distinct integers. You're also given a list of dependencies. A
  dependency is represented as a pair of jobs where the first job is a
  prerequisite of the second one. In other words, the second job depends on the
  first one; it can only be completed once the first job is completed.
  
  Write a function that takes in a list of jobs and a list of dependencies and
  returns a list containing a valid order in which the given jobs can be
  completed. If no such order exists, the function should return an empty array.
'''
#Solution1
def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs,deps)
	return getOrderedJobs(jobGraph)

def createJobGraph(jobs,deps):
	graph = JobGraph(jobs)
	for prereq,job in deps:
		graph.addPrereq(job,prereq)
	return graph

def getOrderedJobs(graph):
	orderedJobs = [] 
	nodes = graph.nodes
	while len(nodes):
		node = nodes.pop() 
		containsCycle = depthFirstTraverse(node,orderedJobs)
		if containsCycle:
			return [] 
	return orderedJobs

def depthFirstTraverse(node,orderedJobs):
	if node.visited:
		return False 
	if node.visiting:
		return True 
	node.visiting = True
	for prereqNode in node.prereqs:
		containsCycle = depthFirstTraverse(prereqNode,orderedJobs)
		if containsCycle:
			return True 
	node.visited = True 
	node.visiting = False 
	orderedJobs.append(node.job) 
	return False 

class JobGraph:
	def __init__(self,jobs):
		self.nodes = [] 
		self.graph = {} 
		for job in jobs:
			self.addNode(job)
	
	def addNode(self,job):
		self.graph[job] = JobNode(job) 
		self.nodes.append(self.graph[job]) 
		
	def addPrereq(self,job,prereq):
		jobNode = self.getNode(job) 
		prereqNode = self.getNode(prereq) 
		jobNode.prereqs.append(prereqNode)
	
	def getNode(self,job):
		if job not in self.graph:
			self.addNode(job)
		return self.graph[job] 
  
  class JobNode:
	def __init__(self,job):
		self.job = job
		self.prereqs = [] 
		self.visited = False 
		self.visiting = False 
    
'''jobs = [1, 2, 3, 4]
   deps = [
  [1, 2],
  [1, 3],
  [3, 2],
  [4, 2],
  [4, 3]
]
'''
