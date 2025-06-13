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
    def __init__(self, url = "", prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def printList(self) -> None:
        current = self.current
        print("Head -> ", end="")
        while current:
            print(current.url, " -> ", end="")
            current = current.next
        print(" Tail")

    def visit(self, url: str) -> None:
        self.current.next = ListNode(url, self.current)
        self.current = self.current.next
        

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        
        return self.current.url
    

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        
        return self.current.url

bh = BrowserHistory("leetcode.com")
# print(bh.printList())
bh.visit("google.com")
# print(bh.printList())
bh.visit("facebook.com")
# print(bh.printList())
bh.visit("youtube.com")
# print(bh.printList())
print(bh.back(1))
# print(bh.printList())
print(bh.back(1))
# print(bh.printList())
print(bh.forward(1))
# print(bh.printList())
bh.visit("linkedin.com")
# print(bh.printList())
print(bh.forward(2))
# print(bh.printList())
print(bh.back(2))
# print(bh.printList())
print(bh.back(7))
# print(bh.printList())