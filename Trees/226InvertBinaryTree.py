'''
Task:

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Set 02

# Set 03

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> [TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
