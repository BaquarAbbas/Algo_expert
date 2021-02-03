'''
  Write a function that takes in a string of words separated by one or more
  whitespaces and returns a string that has these words in reverse order.
  
  Note that you're not  allowed to to use any built-in reverse or built_in methods/Functions.
  However,you are allowed to use buil_in join method/function.
  '''
  #Solution1
  def reverseWordsInString(string):
	words = [] 
	startOfWord = 0 
	for idx in range(len(string)):
		character = string[idx] 
		
		if character == " ":
			words.append(string[startOfWord:idx])
			startOfWord = idx 
		
		elif string[startOfWord] == " ":
			words.append(" ")
			startOfWord = idx
			
	words.append(string[startOfWord:])
	
	reverse(words)
	return "".join(words) 
  
  def reverse(List):
	start,end = 0,len(List) - 1
	while start < end:
		List[start],List[end] = List[end],List[start]
		start += 1
		end -= 1
    
  #Solution2
  def reverseWordsInString(string):
    characters = [char for char in string] 
	reverseListRange(characters,0,len(string)-1) 
	startOfWord = 0 
	while startOfWord < len(characters):
		endOfWord = startOfWord
		while endOfWord < len(characters) and characters[endOfWord] != " ":
			endOfWord += 1 
		reverseListRange(characters,startOfWord,endOfWord -1) 
		startOfWord = endOfWord + 1
	return "".join(characters)
  
  def reverseListRange(list,start,end):
	while start < end:
		list[start],list[end] = list[end],list[start] 
		start += 1 
		end -= 1 
    
'''string = "Algoexpert is the best!"'''
 
  
