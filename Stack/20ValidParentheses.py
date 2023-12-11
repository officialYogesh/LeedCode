'''
Task:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

def isValid(self, s):
  """
  :type s: str
  :rtype: bool
  """
  d = {'(':')', '{':'}','[':']'}
  stack = []
  for i in s:
      if i in d:  # 1
          stack.append(i)
      elif len(stack) == 0 or d[stack.pop()] != i:  # 2
          return False
  return len(stack) == 0 # 3

# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket
'''


# Test Cases
# Set 01
s = "()"
# Set 02
s = "()[]{}"
# Set 03
s = "(]"

from collections import deque

def solution(s):
  s = list(s)
  hashMap = dict({"(": ")", "[": "]", "{": "}"})
  stack = deque()

  for char in s:
    if char in ['(', '[', '{']:
      stack.append(char)
    else:
      top = stack.pop()
      if hashMap[top] != char:
        return False

  return True
  
print(solution(s))
