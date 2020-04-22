"""
*.*.*.*.*.*
Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.

Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
*.*.*.*.*.*

Example:
Input:nums = [1,1,1], k = 2
Output: 2
"""

class Solution:
    def subarraySum(self, nums, k):
        
        # make counter and hash table
        sum_freq, count = {}, 0
        
        # make cumulative sum
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        for cumulative_sum in nums:
            match = cumulative_sum - k
            
            # when sum(subarray[i,j]) == k -> sum(arr[:j]) - sum(arr[:i]), j > i
            if match in sum_freq:
                count += sum_freq[match]
            
            # when cumulative sum == k -> sum(arr[:j]) == k
            if match == 0:
                count += 1
            
            # add cumulative sum to hash table
            if cumulative_sum in sum_freq:
                sum_freq[cumulative_sum] += 1
            
            else:
                sum_freq[cumulative_sum] = 1
                
        return count


if __name__ == "__main__":
    print 'Execute input nums=[1,1,1], k=2 :: ', Solution().subarraySum([1,1,1], 2)
    
