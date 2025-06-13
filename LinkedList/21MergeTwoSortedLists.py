'''
Task:

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Test Cases
# Set 01
list1 = [1,2,4]
list2 = [1,3,4]
# Set 02
list1 = [1,2,4]
list2 = [1,3,4]
# Set 03

class Solution:
      def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         head = current = ListNode()

         while list1 and list2:
            if list1.val < list2.val:
               current.next = list1
               list1 = list1.next
            else:
               current.next = list2
               list2 = list2.next
            current = current.next
         
         if list1:
            current.next = list1
         if list2:
            current.next = list2
         
         return head











class LinkedList:
  def __init__(self, head = None):
    self.head = head
  
  def insertAtEnd(self, data):
    new_node = ListNode(data)
    if self.head is None:
        self.head = new_node
        return

    current_node = self.head
    while(current_node.next):
        current_node = current_node.next

    current_node.next = new_node
  
  def updateHead(self, newHead):
     self.head = newHead


  def printLL(self):
    current_node = self.head
    while(current_node):
        print(current_node.val)
        current_node = current_node.next

def solution(head1, head2):
  dummy = ListNode()
  tail = dummy

  while head1 and head2:
    if head1.val < head2.val:
        tail.next = head1
        head1 = head1.next
    else:
       tail.next = head2
       head2 = head2.next
    tail = tail.next
  
  if head1:
     tail.next = head1
  elif head2:
     tail.next = head2
  
  return dummy.next



# print(solution())
lList1 = LinkedList()
for x in list1:
   lList1.insertAtEnd(x)
lList2 = LinkedList()
for x in list2:
   lList2.insertAtEnd(x)

lList3 = LinkedList(solution(lList1.head, lList2.head)).printLL()
