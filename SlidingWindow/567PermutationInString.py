'''
Task:

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
s1 = "ab"
s2 = "eidbaooo"
# Set 02
s1 = "ab"
s2 = "eidboaoo"

def solution(s1, s2):
  if len(s1) > len(s2):
    return False
  
  s1Count, s2Count = [0] * 26, [0] * 26

  for i in range(len(s1)):
    s1Count[ord(s1[i]) - ord('a')] += 1
    s2Count[ord(s2[i]) - ord('a')] += 1

  matches = 0
  # Initial Matches
  for i in range(26):
    matches += (1 if s1Count[i] == s2Count[i] else 0)

  # Sliding Window
  left = 0
  for right in range(len(s1), len(s2)):
    if matches == 26: return True

    # Right pointer, while adding a new character in s2
    index = ord(s2[right]) - ord('a')
    s2Count[index] += 1
    if s1Count[index] == s2Count[index]: matches += 1
    elif s1Count[index] + 1 == s2Count[index]: matches -= 1

    # Left pointer, while removing a character in s2
    index = ord(s2[left]) - ord('a')
    s2Count[index] -= 1
    if s1Count[index] == s2Count[index]: matches += 1
    elif s1Count[index] - 1 == s2Count[index]: matches -= 1

    left += 1
  
  return matches == 26

print(solution(s1, s2))
