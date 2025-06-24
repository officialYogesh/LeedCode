'''
Task:

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
'''
Code Walkthrough:

'''
'''
Best / Optimized Solution for review:

dic={}
for word in strs:
    sorted_word="".join(sorted(word))
    if sorted_word not in dic:
        dic[sorted_word]=[word]
    else:
        dic[sorted_word].append(word)
return list(dic.values())

'''

# Test Cases
# Set 01


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Set 02
# strs = [""]

# Set 03
# strs = ["a"]


from collections import defaultdict

def solution2(strs):
  hashmap = dict()

  for st in strs:
    sortedS = ''.join(sorted(st))
    if hashmap.get(sortedS, None):
      newS = hashmap.get(sortedS, [])
      newS.append(st)
      hashmap[sortedS] = newS
    else:
      hashmap[sortedS] = [st]
  return list(hashmap.values())


def solution(strs):
  # if len(strs) < 2:
  #   return [strs]
  # hashSet = {}

  # for s in strs:
  #   sortedS = ''.join(sorted(s))
  #   if hashSet.get(sortedS, 0) and sortedS == ''.join(sorted(s)):
  #     newS = hashSet.get(sortedS, [])
  #     newS.append(s)
  #     hashSet[sortedS] = newS
  #   else:
  #     hashSet[sortedS] = [s]

  # return list(hashSet.values())

  res = defaultdict(list)
  
  for s in strs:
    counts = [0] * 26
    for c in s:
      counts[ord(c) - ord('a')] += 1

    res[tuple(counts)].append(s)

  return list(res.values())


print(solution2(strs))
