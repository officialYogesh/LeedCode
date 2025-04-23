'''
Task:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

1. Implement 1 dict, and then iterate through s and add the value count when repeated. On iterating through t if key t is found, minus the value count. And then check for values of the dict for 0, and return True. (Implemented this approach)

2. Sort the string and then compare
'''


# Test Cases
# Set 01
s = "anagram"
t = "nagaram"
# Set 02
# s = "rat"
# t = "car"

def originalSolution(s, t):
  if len(s) != len(t):
    return False
  
  hashSet = {}

  for char in s:
    hashSet[char] = hashSet.get(char, 0) + 1

  for char in t:
    if hashSet.get(char, 0) == 0:
      return False
    else:
      hashSet[char] -= 1

  return True

def solution(s, t):
  if len(s) != len(t):
    return False
  return sorted(s) == sorted(t)
  


print(solution(s, t))
