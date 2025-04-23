'''
Task:

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''


'''
Code Walkthrough:

'''

'''
Best / Optimized Solution for review:

'''

# Test Cases
# Set 01
nums = [1,2,3,1]
# Set 02
# nums = [1,2,3,4]
# Set 03
# nums = [1,1,1,3,3,4,3,2,4,2]

def originalSolution(nums):
  hashMap = set()
  for num in nums:
    if num in hashMap:
      return True
    else:
      hashMap.add(num)
    return False

def solution(nums):
  hashmap = dict()
  for n in nums:
    if(hashmap.get(n, -1) != -1):
      return True
    else:
      hashmap[n] = 1
  return False


print(solution(nums))
