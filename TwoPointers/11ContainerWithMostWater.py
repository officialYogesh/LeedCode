'''
Task:

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
from typing import List


height = [1,8,6,2,5,4,8,3,7]
height = [2,1]
height = [0,2]

class Solution2: #For next practice
  def maxArea(self, heights: List[int]) -> int:
    return 0
















class Solution:
  def maxArea(self, heights: List[int]) -> int:
    maxArea = 0
    l, r = 0, len(heights) - 1
    while l < r:
      distance = r - l
      newArea = distance * min(heights[l], heights[r])
      maxArea = max(maxArea, newArea)
      if heights[l] < heights[r]:
        l += 1
      else:
        r -= 1

    return maxArea

















def solution(height):
  left, right = 0, len(height) - 1
  maxArea = 0

  while left < right:
    maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
    if height[left] < height[right]:
      left += 1
    else:
      right -= 1

  return maxArea

s = Solution()
print(s.maxArea(height))
