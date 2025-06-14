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
n = 2
# Set 02
n = 3
# Set 03
n = 44

class Solution:
  def climbStairs(self, n: int) -> int:
    one, two = 1, 1
    for i in range(n-1):
      temp = one
      one += two
      two = temp
    
    return one
    


solution = Solution()
print(solution.climbStairs(n))
