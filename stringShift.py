"""
*.*.*.*.*.*
You are given a string s containing lowercase English letters, 
and a matrix shift, where shift[i] = [direction, amount]:

* direction can be 0 (for left shift) or 1 (for right shift). 
* amount is the amount by which string s is to be shifted.
* A left shift by 1 means remove the first character of s 
  and append it to the end.
* Similarly, a right shift by 1 means remove the last character of s 
  and add it to the beginning.

Return the final string after all operations.


Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
*.*.*.*.*.*


# Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

# Example 2:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
"""

class Solution:
    def stringShift(self, s, shift):
        # Input: s -> str, shift-> list of list
        # Output: str

        # partition left/right shifts
        left_shifts = [sft[1] for sft in shift if sft[0] == 0]
        right_shifts = [sft[1] for sft in shift if sft[0] == 1]
        
        overall_shifts = sum(left_shifts) - sum(right_shifts)
        

        if overall_shifts > 0:
            # do left shifts
            for _ in range(overall_shifts):
                s = s[1:] + s[0]
        
        elif overall_shifts < 0:
            # do right shifts
            for _ in range(-overall_shifts):
                s = s[-1] + s[:-1]
                
        return s
        

if __name__ == "__main__":
    
    print 'Execute input s = "abc", shift = [[0,1],[1,2]] :: ', Solution().stringShift(s="abc", shift=[[0,1],[1,2]])
    print 'Execute input s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]] :: ', Solution().stringShift(s="abcdefg", shift=[[1,1],[1,1],[0,2],[1,3]])
	
