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
# s = "()[]{}"
# Set 03
# s = "(]"

from collections import deque

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

    for c in s:
      if c in closeToOpen:
        if stack and stack[-1] == closeToOpen[c]:
          stack.pop()
        else:
          return False
      else:
        stack.append(c)
    
    return True if not stack else False

sol = Solution()
print(sol.isValid(s))
