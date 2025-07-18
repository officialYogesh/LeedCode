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

from collections import deque


class MyStack:

    def __init__(self):
      self.q = deque()
        

    def push(self, x: int) -> None:
      self.q.append(x)
      for i in range(len(self.q) - 1):
        self.q.append(self.q.popleft())
        

    def pop(self) -> int:
      return self.q.popleft()
        

    def top(self) -> int:
      return self.q[0]
    
    def empty(self) -> bool:
      return len(self.q) == 0