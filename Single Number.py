"""
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
"""
# Example 1
# Input: [2,2,1]
# Output: 1

# Example 2
# Input: [4,1,2,1,2]
# Output: 4

def singleNumber(nums):
	# input: num-> list
	# output: int
	return (sum(set(nums))*2) - sum(nums)

if __name__ == "__main__":
	print 'Execute input nums=[2,2,1]:: ', singleNumber([2,2,1])
	print 'Execute input nums=[4,1,2,1,2]:: ', singleNumber([4,1,2,1,2])
