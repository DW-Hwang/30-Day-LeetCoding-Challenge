"""
*.*.*.*.*.*
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. 

An island is surrounded by water and is formed by 
connecting adjacent lands horizontally or vertically. 

You may assume all four edges of the grid are all surrounded by water.
*.*.*.*.*.*

# Example 1:
Input:
11110
11010
11000
00000

Output: 1

# Example 2:
Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands(self, grid):
        
        # input grid: List[List[str]]
        # output int

        # count number of islands
        count = 0
        
        def get_neighbours(i, j):
            neighbours = set() # store neighboring island, i.e. same island
            
            # i-index:: vertical elements, j-index:: horizontal elements
            if i > 0 and grid[i-1][j] == '1':
                neighbours.add((i-1, j))
            if i + 1 < len(grid) and grid[i+1][j] == '1':
                neighbours.add((i+1, j))
            if j > 0 and grid[i][j-1] == '1':
                neighbours.add((i, j-1))
            if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
                neighbours.add((i, j+1))
                
            return neighbours
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # iterate over all elements horizontally, vertically
                # if current element is water, i.e. '0' -> do nothing
                # else current element is island, i.e. '1'
                # update count and assign water to prevent double counting in loops
                # get neighbouring island and set water 
                
                if grid[i][j] == '1': # found island
                    count += 1
                    grid[i][j] = '0'
                    neighbours = get_neighbours(i, j)
                
                    while len(neighbours):
                        next_neighbours = set() # create set to store next neighbours
                        for neighbour in neighbours:
                            # make nearby island 0
                            grid[neighbour[0]][neighbour[1]] = '0' 
                            # countinue to search for neighbours and append set (union)
                            next_neighbours |= get_neighbours(neighbour[0], neighbour[1]) 
                        neighbours = next_neighbours
                    
        return count
        

if __name__ == "__main__":
    
    map1 = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
    map2 = [['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1']]

    print 'Execute input grid = exmaple 1 :: ', Solution().numIslands(map1) 
    print 'Execute input grid = example 2 :: ', Solution().numIslands(map2)
	
