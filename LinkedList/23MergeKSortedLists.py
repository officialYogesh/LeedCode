'''
Task:

23. Merge k Sorted Lists
Hard
Topics
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
lists = [[1,4,5],[1,3,4],[2,6]]
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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

linkedLists = []
for x in lists:
  lList = LinkedList()
  for y in x:
    lList.insertAtEnd(x)
  linkedLists.append(lList)

def mergeTwoLinkedLists(lList1, lList2):
  dummy = ListNode()
  tail = dummy

  while lList1 and lList2:
    if lList1.val < lList2.val:
      tail.next = lList1
      lList1 = lList1.next
    else:
      tail.next = lList2
      lList2 = lList2.next
    tail = tail.next
  
  if lList1:
     tail.next = lList1
  if lList2:
     tail.next = lList2
  
  return dummy.next

def solution(lists):
  if not lists or len(lists) == 0:
     return None
  
  while len(lists) > 1:
    mergedLists = []
    for i in range(0, len(lists), 2):
      lList1 = lists[i]
      lList2 = lists[i + 1] if (i + 1) > len(lists) else None
      mergedLists.append(mergeTwoLinkedLists(lList1, lList2))
    lists = mergedLists
  
  return lists[0]


print(solution(linkedLists))
