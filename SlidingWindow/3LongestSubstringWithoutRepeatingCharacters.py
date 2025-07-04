'''
Task:

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
s = "abcabcbb"
# Set 02
s = "bbbbb"
# # Set 03
s = "pwwkew"
# Set 04
s = "aab"

class Solution2: #For next practice
  def lengthOfLongestSubstring(self, s: str) -> int:

    return 0



















class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    res = 0
    left = 0

    for right in range(len(s)):
      while s[right] in charSet:
        charSet.remove(s[left])
        left += 1
      charSet.add(s[right])
      res = max(res, right - left + 1)

    return res

def solution(s):
  res = 0
  left = 0
  charSet = set()

  for right in range(len(s)):
    while s[right] in charSet:
      charSet.remove(s[left])
      left += 1
    charSet.add(s[right])
    res = max(res, right - left + 1)
  
  return res

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
