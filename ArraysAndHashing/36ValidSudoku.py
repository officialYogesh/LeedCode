import collections
from typing import List
'''
Task:

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:
https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''
'''
Code Walkthrough:

'''
'''
Best / Optimized Solution for review:

'''

# Test Cases
# Set 01
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# Set 02
# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

class Solution2: #For next practice
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    return False
























class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    boxes = collections.defaultdict(set)

    for r in range(9):
      for c in range(9):
        if board[r][c] == '.':
          continue
        if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[(r//3, c//3)]:
          return False
        rows[r].add(board[r][c])
        columns[c].add(board[r][c])
        boxes[(r//3, c//3)].add(board[r][c])

    return True

def solution2(board):
  rows = collections.defaultdict(set)
  columns = collections.defaultdict(set)
  boxes = collections.defaultdict(set)

  for r in range(9):
    for c in range(9):
      if board[r][c] == ".":
        continue
      if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[(r//3, c//3)]:
        return False
      columns[c].add(board[r][c])
      rows[r].add(board[r][c])
      boxes[(r//3, c//3)].add(board[r][c])
  return True



def solution(board):
  columns = collections.defaultdict(set)
  rows = collections.defaultdict(set)
  boxes = collections.defaultdict(set)

  for r in range(9):
    for c in range(9):
      if board[r][c] == ".":
        continue
      if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][
          c] in boxes[(r // 3, c // 3)]:
        return False
      columns[c].add(board[r][c])
      rows[r].add(board[r][c])
      boxes[(r // 3, c // 3)].add(board[r][c])

  return True


s = Solution()
print(s.isValidSudoku(board))
