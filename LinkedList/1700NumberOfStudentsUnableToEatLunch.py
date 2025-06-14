'''
Task:

'''


'''
Code Walkthrough:

'''


'''
Best / Optimized Solution for review:

'''
from typing import List





# Test Cases
# Set 01
students = [1,1,0,0]
sandwiches = [0,1,0,1]
# Set 02
# students = [1,1,1,0,0,1]
# sandwiches = [1,0,0,0,1,1]
# Set 03


class Solution:
  def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    counts = {}

    for student in students:
      counts[student] = counts.get(student, 0) + 1
    
    for sandwich in sandwiches:
      count = counts.get(sandwich, 0)
      if count == 0:
        return counts.get(0, 0) if sandwich == 1 else counts.get(1, 0)
      else:
        counts[sandwich] -= 1
    return 0

solution = Solution()
print(solution.countStudents(students, sandwiches))
