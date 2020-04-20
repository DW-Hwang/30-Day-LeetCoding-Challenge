"""
*.*.*.*.*.*
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val,
and any descendant of node.right has a value > node.val. 
Also recall that a preorder traversal displays the value of the node first,
then traverses node.left, then traverses node.right.)

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
*.*.*.*.*.*

Example: 1
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Explanation:            8
                   5         10
                1     7   N      12
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        
        # empty list
        if not preorder:
            return None
        
        # init tree
        tree, i = TreeNode(preorder[0]), 1
        
        while i < len(preorder) and preorder[i] < tree.val:
            i += 1
        
        tree.left = self.bstFromPreorder(preorder[1:i])
        tree.right = self.bstFromPreorder(preorder[i:])
        
        return tree

if __name__ == "__main__":
    print 'Execute input preorder = [8,5,1,7,10,12] :: ', Solution().bstFromPreorder([8,5,1,7,10,12])
    
