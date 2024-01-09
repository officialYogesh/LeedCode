'''
Task:

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:
https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
head = [1,2,3,4]
# Set 02
head = [1,2,3,4,5]
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

def solution(head):
  slow, fast = head, head.next

  # While fast is not null and fast has not reached the end of list
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  second = slow.next
  previous = slow.next = None
  while second:
     nxt = second.next
     second.next = previous
     previous = second
     second = nxt
  
  first, second = head, previous
  while second:
     firstNext, secondNext = first.next, second.next
     first.next = second
     second.next = firstNext
     first, second = firstNext, secondNext


lList = LinkedList()
for x in head:
   lList.insertAtEnd(x)

solution(lList.head)

lList.printLL()
