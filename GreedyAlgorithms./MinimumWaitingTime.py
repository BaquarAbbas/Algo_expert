'''
  You're given a non-empty array of positive integers representing the amounts
  of time that specific queries take to execute. Only one query can be executed
  at a time, but the queries can be executed in any order.
  
  Write a function that returns the minimum amount of total waiting time for all
  of the queries. For example, if you're given the queries of durations [1,4,5], 
  then the total waiting time if the queries were executed in the order of [5,1,4] 
  would be (0) + (5) + (5+1). The first query of duration 5 would be executed 
  immediately,so the waiting time would be 0, the second query of duration 1 
  would have to wait 5  seconds (the duration of the first query) to be executed, and
  the last query would have to wait the duration of the first two queries before
  being executed.
'''
#Solution
def minimumWaitingTime(queries):
	queries.sort() 
	totalWaitingTime = 0 
	for idx, duration in enumerate(queries):
		queriesLeft = len(queries) - (idx + 1) 
		totalWaitingTime += duration * queriesLeft 
		
	return totalWaitingTime
