'''
Task:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

From NeetCode.io

def solution(l1, l2):
  dummy = ListNode()
  current = dummy
  carry = 0

  while l1 or l2 or carry:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0

    # New Digit
    val = v1 + v2 + carry
    carry = val // 10
    val = val % 10
    current.next = ListNode(val)

    # Update pointers
    current = current.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None

  return dummy.next
'''


# Test Cases
# Set 01
l1 = [2,4,3]
l2 = [5,6,4]
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


  def printLL(self, head = None):
    current_node = head if head else self.head
    while(current_node):
        print(current_node.val)
        current_node = current_node.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printLL(self, head):
      current_node = head
      while(current_node):
          print(current_node.val)
          current_node = current_node.next


def solution(l1, l2):
  head1 = l1
  head2 = l2

  number1 = number2 = ''
  
  while head1:
      number1 += str(head1.val)
      head1 = head1.next
  while head2:
      number2 += str(head2.val)
      head2 = head2.next

  number1 = number1[::-1]
  number2 = number2[::-1]

  dummy = ListNode()
  dummyHead = dummy

  for char in str(int(number1) + int(number2))[::-1]:
      dummy.next = ListNode(int(char))
      dummy = dummy.next

  return dummyHead.next


lList1 = LinkedList()
lList2 = LinkedList()

for x in l1:
   lList1.insertAtEnd(x)
for x in l2:
   lList2.insertAtEnd(x)

list3 = LinkedList()
list3.printLL(solution(lList1.head, lList2.head))