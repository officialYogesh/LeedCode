'''
Task:

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
nums = [100,4,200,1,3,2]
# Set 02
nums = [0,3,7,2,5,8,4,6,0,1]
# Set 03
# nums = [1,0,1,2]
# Set 04
# nums = []

import heapq

class Solution:
    def longestConsecutive(self, nums):
        if not len(nums):
            return 0
        
        heap = []
        maxConsecutiveSeq = 1
        new = 1
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
        for i in range(len(nums)-1):
            last = heapq.heappop(heap)
            current = heapq.heappop(heap)
            if last == current:
                heapq.heappush(heap, current)
                continue
            if last+1 == current:
                new += 1
            else:
                new = 1
            if maxConsecutiveSeq < new:
                maxConsecutiveSeq = new
            heapq.heappush(heap, current)
        
        return maxConsecutiveSeq
                
    def longestConsecutiveOptimized(self, nums):
        numsSet = set(nums)
        longest = 0
        for n in numsSet:
            if n-1 not in numsSet:
                length = 0
                while n+length in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest


s = Solution()
print(s.longestConsecutive(nums))
print(s.longestConsecutiveOptimized(nums))
