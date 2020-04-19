"""
*.*.*.*.*.*
Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. 
If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
*.*.*.*.*.*

# Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

# Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:
    def search(self, nums, target):
        # input: nums-> list, target-> int
        # output: int
        
        # case 1: when list is empty 
        if len(nums) == 0:
            return -1
        
        # when list contains 1 or more integer
        # make index
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
    
            if target == nums[mid]:
                return mid
            
            # look at left if left is sorted
            if nums[left] < nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid -1
                
                else:
                    left = mid + 1
            
            # look at right 
            else:
                if nums[mid + 1] <= target and target <= nums[right]:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
        return left if nums[left] == target else -1

if __name__ == "__main__":
    
    print 'Execute input nums = [4,5,6,7,0,1,2], target = 0 :: ', Solution().search([4,5,6,7,0,1,2], 0)
    print 'Execute input nums = [4,5,6,7,0,1,2], target = 3 :: ', Solution().search([4,5,6,7,0,1,2], 3)
   
	
