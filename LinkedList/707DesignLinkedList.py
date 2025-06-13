'''
Task:

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01

# Set 02

# Set 03
class ListNode:
    def __init__(self, val=0, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class MyLinkedList:

    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def printList(self) -> None:
        current = self.left.next
        print("Head -> ", end="")
        while current:
            print(current.val, " -> ", end="")
            current = current.next
        print(" Tail")

    def get(self, index: int) -> int:
        current = self.left.next
        while current and index > 0:
            index -= 1
            current = current.next
        if current and index == 0 and current != self.right:
            return current.val
        else: return -1

    def addAtHead(self, val: int) -> None:
        node, prev, nxt = ListNode(val), self.left, self.left.next
        prev.next = node
        nxt.prev = node # type: ignore
        node.prev= prev
        node.next = nxt

    def addAtTail(self, val: int) -> None:
        node, prev, nxt = ListNode(val), self.right.prev, self.right
        prev.next = node # type: ignore
        nxt.prev = node
        node.prev = prev
        node.next = nxt
        
    
    def addAtIndex(self, index: int, val: int) -> None:
        current = self.left.next
        while current and index > 0:
            index -= 1
            current = current.next
        if current and index == 0:
            node, prev, nxt = ListNode(val), current.prev, current
            prev.next = node
            nxt.prev = node
            node.next = nxt
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        current = self.left.next
        while current and index > 0:
            index -= 1
            current = current.next
        if current and current != self.right and index == 0:
            prev, nxt = current.prev, current.next
            nxt.prev = prev
            prev.next = nxt


obj = MyLinkedList()
obj.printList()
obj.addAtHead(1)
obj.printList()
obj.addAtTail(3)
obj.printList()
obj.addAtIndex(1,2)
obj.printList()
print(obj.get(1))
obj.printList()
obj.deleteAtIndex(1)
obj.printList()
print(obj.get(1))
obj.printList()