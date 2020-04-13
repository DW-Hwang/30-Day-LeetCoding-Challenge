"""
*.*.*.*.*.*
Given a binary array, find the maximum length 
of a contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
*.*.*.*.*.*


# Example 1
Input: [0,1]
Output: 2
Explanation: 
[0, 1] is the longest contiguous subarray
 with equal number of 0 and 1.f last stone.

 # Example 2
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is 
a longest contiguous subarray with equal number of 0 and 1.

"""

class Solution:
    def findMaxLength(self, nums):
        # make counter, max_length
        counter, max_length = 0, 0

        # counter dictionary
        count_dict = {0:0}

        for i, binary in enumerate(nums):
            counter += (2*binary) - 1

            if counter in count_dict:
                max_length = max(max_length, i+1 - count_dict[counter])
            
            else:
                count_dict[counter] = i+1

        return max_length


if __name__ == "__main__":
    
    print 'Execute input nums=[0,1] :: ', Solution().findMaxLength([0,1])
    print 'Execute input nums=[0,1,0] :: ', Solution().findMaxLength([0,1,0])

	
