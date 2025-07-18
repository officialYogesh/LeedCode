'''
Task:

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
'''
Code Walkthrough:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

l = 1, r = 1
output = [1,1,1,1]

i = 1:
output: output[i-1] = nums[i] * l
output: [2,1,1,1]
l = 2


for i in range nums:
  nums[i] *= l
  l *= nums[i]

  
  


'''
'''
Best / Optimized Solution for review:

'''

# Test Cases
# Set 01
nums = [1,2,3,4]
# Set 02
# nums = [-1,1,0,-3,3]


class Solution:
  def solutionPractice4(self, nums):
    pass
























  
  def solution3(self, nums):
    res = [1] * len(nums)
    prefix, postfix = 1,1

    for i in range(len(nums)):
      res[i] = prefix
      prefix *= nums[i]

    for i in range(len(nums) - 1, -1, -1):
      res[i] *= postfix
      postfix *= nums[i]
    
    return res

  def solution(self, nums):
    output = [1] * len(nums)
    prefix, postfix = 1,1
    
    for i in range(len(nums)):
      output[i] = prefix
      prefix *= nums[i]

    for i in range(len(nums) - 1, -1, -1):
      output[i] *= postfix
      postfix *= nums[i]

    return output

s = Solution()
print(s.solution(nums))
