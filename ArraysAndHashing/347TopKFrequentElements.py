'''
Task:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

Can explore heap
'''


# Test Cases
# Set 01
import heapq


nums = [1,1,1,2,2,3]
k = 2

def solution2(nums, k):
  counts = {}

  for num in nums:
    counts[num] = 1 + counts.get(num, 0)
  
  heap = []
  for num in counts.keys():
    heapq.heappush(heap, (counts[num], num))
    if len(heap) > k:
      heapq.heappop(heap)
  
  res = []
  for i in range(k):
    res.append(heapq.heappop(heap)[1])
  
  return res

def solution(nums, k):
  # hashSet = {}
  
  # for n in nums:
  #   hashSet[n] = hashSet.get(n, 0) + 1

  # rSorted = sorted(hashSet.items(), key=lambda x: x[1], reverse=True)
  # return [x[0] for x in rSorted[:k]]
    
  counts = {}
  for num in nums:
    counts[num] = 1 + counts.get(num, 0)

  heap = []
  for num in counts.keys():
    heapq.heappush(heap, (counts[num], num))
    if len(heap) > k:
      heapq.heappop(heap)
  
  res = []
  for i in range(k):
    res.append(heapq.heappop(heap)[1])
  
  return res


print(solution2(nums, k))
