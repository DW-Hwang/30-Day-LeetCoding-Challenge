"""
*.*.*.*.*.*
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is 
equal to the product of all the elements of nums except nums[i].

Constraint: 
It's guaranteed that the product of the elements 
of any prefix or suffix of the array (including the whole array) 
fits in a 32 bit integer.

Note: 
Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose 
of space complexity analysis)
*.*.*.*.*.*

# Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
"""

class Solution1:
    def productExceptSelf(self, nums):
        # Input: nums -> list[int]
        # Output: list[int]

        output = [1] * len(nums)
        left, right = 1, 1

        for i in range(len(nums)):
            output[i] *= left
            output[-i-1] *= right
            left *= nums[i]
            right *= nums[-i-1]

        return output


# Alternatively, we separate the above steps into 2 loops.
# The first is a forward loop and second is a backward loops
class Solution2:
    def productExceptSelf(self, nums):
        # Input: nums -> list[int]
        # Output: list[int]

        output = [1] * len(nums)

        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]

        right = 1
        
        for i in list(range(0, len(nums)))[::-1]:
            output[i] *= right
            right *= nums[i]

        return output
        

if __name__ == "__main__":
    
    print '(Solution 1) Execute input nums = [1,2,3,4] :: ', Solution1().productExceptSelf([1,2,3,4])
    print '(Solution 2) Execute input nums = [1,2,3,4] :: ', Solution2().productExceptSelf([1,2,3,4])
	
