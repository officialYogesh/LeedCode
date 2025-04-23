'''
Task:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
nums = [2,7,11,15]
target = 9

# Set 02
# nums = [3,2,4]
# target = 6

# Set 03
# nums = [3,3]
# target = 6

def solution2(nums, target):
  hashmap = dict()

  for i, num in enumerate(nums):
    if hashmap.get((target - num), -1) != -1:
      return [hashmap.get((target - num)), i]
    hashmap[num] = i

def solution(nums, target):
  prevMap = {}
  for i, n in enumerate(nums):
    diff = target - n
    if diff in prevMap:
      return [prevMap[diff], i]
    prevMap[n] = i


print(solution2(nums, target))
