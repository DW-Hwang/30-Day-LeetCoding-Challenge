"""
*.*.*.*.*.*
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.
The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed,
and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.
Return the weight of this stone (or 0 if there are no stones left.)

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
*.*.*.*.*.*


# Example 
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""

class Solution1:
    def lastStoneWeight(self, stones):
        
        # empty list
        if len(stones) == 0:
            return 0
        
        # last stone in list
        elif len(stones) == 1:
            return stones[0]
        
        else:
            stones = sorted(stones)
            # destroy 2 heaviest stones
            smashing_stone1, smashing_stone2 = stones.pop(), stones.pop()
            stones.append(smashing_stone1 - smashing_stone2)

            return self.lastStoneWeight(stones)



class Solution2:
    def lastStoneWeight(self, stones):
        
        # make global list
        self.stones = stones
        
        while len(self.stones) > 1:    
            smashing_stone1 = self.popLargest()
            smashing_stone2 = self.popLargest()
            self.stones.append(smashing_stone1-smashing_stone2)
            
        # empty list
        if len(self.stones) == 0:
            return 0
        
        # last stone in list
        elif len(self.stones) == 1:
            return self.stones[0]
            
        
    def popLargest(self):
        large_stone_index = self.stones.index(max(self.stones))
        return self.stones.pop(large_stone_index)


if __name__ == "__main__":
    
    stones = [2,7,4,1,8,1]

    print '(Solution 1) Execute input stones=[2,7,4,1,8,1]:: ', Solution1().lastStoneWeight(stones)
    print '(Solution 2) Execute input stones=[2,7,4,1,8,1]:: ', Solution2().lastStoneWeight(stones)

	
