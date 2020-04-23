"""
*.*.*.*.*.*
Given a range [m, n] where 0 <= m <= n <= 2147483647,
return the bitwise AND of all numbers in this range, inclusive.
*.*.*.*.*.*

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
"""

class Solution:
    def rangeBitwiseAnd(self, m, n):
        
        if m == n:
            return n
        
        elif m < n:
            reduced_n = n - (n & -n)
            return self.rangeBitwiseAnd(m, reduced_n)
        
        return n

if __name__ == "__main__":
    print 'Execute input m = 5, n = 7 :: ', Solution().rangeBitwiseAnd(m=5, n=7)
    print 'Execute input m = 0, n = 1 :: ', Solution().rangeBitwiseAnd(m=0, n=1)
    
