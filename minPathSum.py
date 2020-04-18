"""
*.*.*.*.*.*
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes 
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
*.*.*.*.*.*

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7

Explanation: Because the path 1->3->1->1->1 minimizes the sum.
"""

class Solution:
     def minPathSum(self, grid):

        # case for empty grid
        if len(grid) == 0:
            return 0

        height, width = len(grid), len(grid[0])

        for i in range(height):
            for j in range(width):
                # for first element, i.e. i = j = 0 -> do nothing
                # for element[i][j], update with adding 
                # previous (from top or left) minimum
                if i == 0 and j == 0:
                    continue
                
                # for leftmost column
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                
                # for top row
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[height-1][width-1]

        

if __name__ == "__main__":
    print 'Execute input grid = [[1,3,1],[1,5,1],[4,2,1]] :: ', Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    
