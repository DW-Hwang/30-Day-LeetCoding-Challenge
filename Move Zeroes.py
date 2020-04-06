"""
Given an array nums, write a function to move all 0's 
to the end of it while maintaining the relative order 
of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# Example 1
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Solution 1: For loop
def moveZeroes1(nums):

	count = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[count], nums[i] = nums[i], nums[count]
			count += 1

	print(nums)

# Solution 2: While loop
def moveZeroes2(nums):
	# input: nums->list
	# output: None
	i = count = 0
	while i < len(nums) and count < (len(nums)):
		if nums[i] == 0:
			while count < (len(nums) - 1) and nums[count] == 0:
				count += 1
			nums[i], nums[count] = nums[count], 0
        
		i += 1
		count += 1
	print(nums)


if __name__ == "__main__":
	print '(Solution 1) Execute input nums=[0,1,0,3,12]:: ', moveZeroes1([0,1,0,3,12])
	print '(Solution 2) Execute input nums=[0,1,0,3,12]:: ', moveZeroes2([0,1,0,3,12])

