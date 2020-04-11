"""
*.*.*.*.*.*
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is 
the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Note: 
The length of path between two nodes is
represented by the number of edges between them.
*.*.*.*.*.*


# Example 
Given a binary tree 
test = TreeNode(1)
test.left = TreeNode(2)
test.left.left = TreeNode(4)
test.left.right = TreeNode(5)
test.right = TreeNode(3)

output-> 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        # create global counter
        self.count = 0
        def depth(root):
            if not root:
                return 0
                
            L = depth(root.left)
            R = depth(root.right)
            self.count = max(self.count, L+R)
                
            return max(L, R) + 1
        depth(root)
            
        return self.count      


if __name__ == "__main__":
    
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.left.left = TreeNode(4)
    test.left.right = TreeNode(5)
    test.right = TreeNode(3)

    print 'Execute root = the example tree :: ', Solution().diameterOfBinaryTree(test)

	
