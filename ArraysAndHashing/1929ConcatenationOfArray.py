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
nums = [1,2,1]
# Set 02
nums = [1,3,2,1]
# Set 03

from typing import List


class Solution:
  def getConcatenation(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * (2*n)

    for i in range(n):
      ans[i] = nums[i]
      ans[i+n] = nums[i]
    
    return ans


solution = Solution()
print(solution.getConcatenation(nums))
