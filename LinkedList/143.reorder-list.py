# 
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (62.60%)
# Likes:    11832
# Dislikes: 461
# Total Accepted:    1.3M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# Reorder the list to be on the following form:
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
# 
# 
#

# type: ignore

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        s1, s2 = head, prev

        while s2:
            temp1 = s1.next
            temp2 = s2.next
            s1.next = s2
            s2.next = temp1
            s2 = temp2
            s1 = temp1
        
# @lc code=end

