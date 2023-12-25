'''
Task:

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

ans = [0] * len(temperatures)
stack = []
for day, temp in enumerate(temperatures):
    while stack and temp > temperatures[stack[-1]]:
        ans[prev_day] = day - (prev_day := stack.pop())
    stack.append(day)
return ans

'''


# Test Cases
# Set 01
temperatures = [73,74,75,71,69,72,76,73]
# Set 02
temperatures = [30,40,50,60]
# Set 03
temperatures = [30,60,90]

def solution(temperatures):
  res = [0] * len(temperatures)
  stack = []

  for i, t in enumerate(temperatures):
    while stack and t > stack[-1][0]:
      stackT, stackInd = stack.pop()
      res[stackInd] = i - stackInd
    stack.append([t, i])

  return res


print(solution(temperatures))
