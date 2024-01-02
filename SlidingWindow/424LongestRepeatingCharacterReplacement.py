'''
Task:

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length


'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

def solution(s, k):
  left = 0
  res = 0
  maxF = 0
  frequency = {}

  for right in range(len(s)):
    frequency[s[right]] = frequency.get(s[right], 0) + 1
    maxF = max(maxF, frequency[s[right]])

    while (right - left + 1) - maxF > k:
      frequency[s[left]] -= 1
      left += 1
    
    res = max(res, (right - left + 1))

  return res
'''


# Test Cases
# Set 01
s = "ABAB"
k = 2
# Set 02
s = "AABABBA"
k = 1
# Set 03

def solution(s, k):
  frequency = {}
  res = 0
  left = 0

  for right in range(len(s)):
    frequency[s[right]] = 1 + frequency.get(s[right], 0)

    while (right - left + 1) - max(frequency.values()) > k:
      frequency[s[left]] -= 1
      left += 1

    res = max(right - left + 1, res)

  return res

print(solution(s, k))
