"""
Given an integer array arr, 
count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

Constraints:

1 <= arr.length <= 1000
0 <= arr[i] <= 1000
"""

# Example 1
# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

# Example 2
# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

# Example 3
# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

def countElements(arr):
	# input: arr-> list
	# output: int
	count = 0
	checklist = set(arr)
	for num in arr:
		if num+1 in checklist:
			count += 1

	return count 

# Alternatively
def countElements2(arr):
	# input: arr-> list
	# output: int
	checklist = set(arr)
	return sum([num+1 in checklist for num in arr])



if __name__ == "__main__":
	print 'Execute input arr=[1,2,3]:: ', countElements([1,2,3])
	print 'Execute input arr=[1,1,3,3,5,5,7,7]:: ', countElements([1,1,3,3,5,5,7,7])
	print 'Execute input arr=[1,3,2,3,5,0]:: ', countElements([1,3,2,3,5,0])
	
