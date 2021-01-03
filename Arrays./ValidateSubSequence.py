'''
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.
'''
#Solution1
def isValidSubsequence(array, sequence):
    seqIdx = 0
	for value in array:
		if seqIdx == len(sequence):
			return True
		if sequence[seqIdx] == value:
			seqIdx += 1
	return seqIdx == len(sequence)
