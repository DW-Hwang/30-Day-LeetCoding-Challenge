"""
Given an integer array nums, 
find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""

# Example 1
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6

def maxSubArray(nums):
	# input: nums->list
	# output: int
	local_max = 0
	global_max = -float('inf')

	for i in nums:
		local_max = max(i, local_max+i)
		global_max = max(local_max, global_max)

	return global_max

if __name__ == "__main__":
	print 'Execute input nums=[-2,1,-3,4,-1,2,1,-5,4]:: ', maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
