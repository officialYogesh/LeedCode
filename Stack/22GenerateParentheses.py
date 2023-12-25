'''
Task:

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
n = 3
# Set 02
n = 2

def solution(n):
  res = []

  def backtrack(openN, closeN, path):
    if openN == closeN == n:
      res.append(path)
      return 
    
    if openN < n:
      backtrack(openN + 1, closeN, path + "(")

    if closeN < openN:
      backtrack(openN, closeN + 1, path + ")")

  
  backtrack(0,0, "")

  return res


print(solution(n))
