#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (67.97%)
# Likes:    12081
# Dislikes: 150
# Total Accepted:    1.3M
# Total Submissions: 2M
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' + '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
# 
# Implement the Trie class:
# 
# 
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
# 
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
# 
# 
#

# @lc code=start

class TrieNode:
   def __init__(self):
      self.children = {}
      self.endOfWord = False

class Trie:

   def __init__(self):
      self.root = TrieNode()

   def insert(self, word: str) -> None:
      current = self.root

      for char in word:
         if char not in current.children:
            current.children[char] = TrieNode()
         current = current.children[char]

      current.endOfWord = True

   def search(self, word: str) -> bool:
      current = self.root
      for char in word:
         if char not in current.children:
            return False
         current = current.children[char]
      
      return current.endOfWord
        

   def startsWith(self, prefix: str) -> bool:
      current = self.root
      for char in prefix:
         if char not in current.children:
            return False
         current = current.children[char]
      
      return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

