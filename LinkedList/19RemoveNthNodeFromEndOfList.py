'''
Task:

Given the head of a linked list, remove the nth node from the end of the list and return its head. 

Example 1:
https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
head = [1,2,3,4,5]
n = 2
# Output: [1,2,3,5]
# Set 02

# Set 03

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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head, n):
  dummy = ListNode(0, head)
  left = dummy
  right = head

  while n:
     right = right.next
     n -= 1
  
  while right:
     left = left.next
     right = right.next
  
  left.next = left.next.next

  return dummy.next


lList = LinkedList()
for x in head:
   lList.insertAtEnd(x)

lList2 = LinkedList(solution(lList.head, n))
lList2.printLL()
