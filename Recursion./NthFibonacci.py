'''
    The Fibonacci sequence is defined as follows: the first number of the sequence is 0 and second number of sequence is 1 
    and  nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth 
    Fibonacci number.
'''

#solution1 
def getNthFib(n):
    if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n-1) + getNthFib(n-2)
    
#solution2 
def getNthFib(n,memorize = {1:0,2:1}):
    if n in memorize:
		return memorize[n]
	else:
		memorize[n] = getNthFib(n - 1,memorize) + getNthFib(n-2,memorize)
		return memorize[n]
