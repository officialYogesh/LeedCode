'''
Task:

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
'''
Code Walkthrough:

'''
'''
Best / Optimized Solution for review:

def isPalindrome(self, s: str) -> bool:
i, j = 0, len(s) - 1
while i < j:
    a, b = s[i].lower(), s[j].lower()
    if a.isalnum() and b.isalnum():
        if a != b:
            return False
        else:
            i, j = i + 1, j - 1
            continue
    i, j = i + (not a.isalnum()), j - (not b.isalnum())
return True
'''

# Test Cases
# Set 01
s = "A man, a plan, a canal: Panama"
# Set 02
s = "race a car"


def solution(s):
  alphanumericString = []
  for char in s:
    if char.isalpha() or char.isnumeric():
      alphanumericString.append(char.lower())

  # Alternative solution
  for i in range(len(alphanumericString) // 2):
    if alphanumericString[i] != alphanumericString[-i - 1]:
      return False

  # Solution using two pointers
  j = len(alphanumericString) - 1
  for i in range(len(alphanumericString) // 2):
    if alphanumericString[i] != alphanumericString[j]:
      return False
    j -= 1

  return True


print(solution(s))
