'''
  Write a function that takes in a non-empty string and that returns a boolean
  representing whether the string is a palindrome.
  
  A palindrome is defined as a string that's written the same forward and
  backward. Note that single-character strings are palindromes.
'''
#Solution1
def isPalindrome(string):
    return string[::-1] == string
  
#Solution2
def isPalindrome(string):
    i = 0
	j = len(string) - 1
	while i < j:
		if string[i] == string[j]:
			j -= 1
		    i += 1
		else:
			return False
		
	return string[i] == string[j]

#Solution3
def isPalindrome(string,i = 0):
	j = len(string) - 1 - i
	if i >=j:
		return True
	elif string[i] != string[j]:
		return False
	else:
		return isPalindrome(string,i+1)
