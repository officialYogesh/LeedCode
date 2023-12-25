'''
Task:

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example Image 1
https://assets.leetcode.com/uploads/2020/10/05/mat.jpg

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example Image 2
https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''


# Test Cases
# Set 01
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# Set 02
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
# Set 03
matrix = [[1]]
target = 0

def solution(matrix, target):
    top, bottom = 0, len(matrix) - 1
    row = top + ((bottom - top) // 2)

    while top <= bottom:
        row = top + ((bottom - top) // 2)
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
          bottom = row - 1
        else:
            break
    
    if not (top <= bottom):
        return False
    
    left, right = 0, len(matrix[0]) - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        if target > matrix[row][mid]:
            left = mid + 1
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return True
        
    return False
        


print(solution(matrix, target))
