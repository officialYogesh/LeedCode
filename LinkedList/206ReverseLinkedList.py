'''
Task:

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:

https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

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
# Set 02

# Set 03

class LinkedList:
  def __init__(self):
    self.head = None
  
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

    

# Iterative Solution
def solution(head):
  prev, current = None, head
  while current:
     nxt = current.next
     current.next = prev
     prev = current
     current = nxt
  
  return prev

def recursive(head):
   if not head or not head.next:
      return head
   
   newHead = recursive(head.next)

   head.next.next = head
   head.next = None

   return newHead

llist = LinkedList()
for x in head:
   llist.insertAtEnd(x)

# llist.updateHead(solution(llist.head))
llist.updateHead(recursive(llist.head))
llist.printLL()
