#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (75.39%)
# Likes:    12136
# Dislikes: 244
# Total Accepted:    1.9M
# Total Submissions: 2.5M
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given the root of a binary search tree, and an integer k, return the k^th
# smallest value (1-indexed) of all the values of the nodes in the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
# 
# 
# 
# Follow up: If the BST is modified often (i.e., we can do insert and delete
# operations) and you need to find the kth smallest frequently, how would you
# optimize?
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            
            current = current.right

        
# @lc code=end

