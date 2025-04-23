'''
Task:
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
strs = ["neet","code","love","you"]
# Set 02
strs = ["we","say",":","yes","!@#$%^&*()"]
# Set 03

class Solution2:
    def encode(self, strs):
        encodedString = ''
        for s in strs:
            encodedString += str(len(s)) + "#" + (s)
        return encodedString

    def decode(self, s):
        decodedList = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = 1 + j
            j = i + length
            decodedList.append(s[i:j])
            i = j

        return decodedList

sol = Solution2()
print(sol.encode(strs))
print(sol.decode(sol.encode(strs)))


from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        ss = ""
        for s in strs:
            ss += str(len(s)) + "#" + s
        return ss

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

s = Solution()
encodedString = s.encode(strs)
# print(encodedString)
decodedList = s.decode(encodedString)
# print(decodedList)
