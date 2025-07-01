#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (37.35%)
# Likes:    9845
# Dislikes: 496
# Total Accepted:    799.9K
# Total Submissions: 2.1M
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  # '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
# 
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# 
# 
# Example 2:
# 
# 
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# 
# 
#

from typing import List

# @lc code=start

class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        current = self
        
        for char in word:
            if char not in current.children:
                current.children[char] = TreeNode()
            current = current.children[char]
        current.word = True

class Solution:
    def __init__(self):
        self.root = TreeNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visited = set(), set()
        ROWS, COLS = len(board), len(board[0])

        for word in words:
          self.root.addWord(word)
      

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children
                ): return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            
            word += board[r][c]
            if node.word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            visited.remove((r, c))
          
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, self.root, "")
        
                      
        return list(res)
                
      
        
# @lc code=end

