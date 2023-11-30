'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


'''
Faster solution:

def majorityElement(self, nums: List[int]) -> int:
  half = len(nums) / 2
  counts = {}
  for num in nums:
      if num not in counts:
          counts[num] =  0
      counts[num] += 1
      if counts[num] > half:
          return num
'''

# set 01
nums = [3,2,3]

# set 02
nums = [2,2,1,1,1,2,2]

def majorityElement(nums: list[int]) -> int:
  n = len(nums)
  threshold = n // 2

  hashmap = {}

  for i in range(0, n):
    if (hashmap.get(nums[i], 0) + 1) > threshold:
      return nums[i]
    else:
      hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
  return 0


output = majorityElement(nums)
print(output)
