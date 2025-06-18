'''
Task:

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
s = "ADOBECODEBANC" 
t = "ABC"
# Set 02

# Set 03

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if t == "" or len(s) < len(t): return ""
    countT, window = {}, {}

    for ch in t:
      countT[ch] = countT.get(ch, 0) + 1

    res, resLen = "", float("inf")
    have, need = 0, len(countT)
    left = 0
    
    for right in range(len(s)):
      ch = s[right]
      window[ch] = window.get(ch, 0) + 1
      if ch in countT and countT[ch] == window[ch]:
        have += 1
        while have == need:
          if (right - left + 1) < resLen:
            res = s[left: right+1]
            resLen = (right - left + 1)
          window[s[left]] -= 1
          if s[left] in countT and window[s[left]] < countT[s[left]]:
            have -= 1
          left += 1
    
    return res

solution = Solution()
print(solution.minWindow(s, t))
