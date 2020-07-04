"""
You are given an array x of n positive numbers. You start at point (0,0) and
moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the
south, x[3] metres to the east and so on. In other words, after each move your direction
changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
"""

from typing import List
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        for i in range(3, len(x)):
            # Fourth line crosses first line and onward
            if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
                return True
            # Fifth line meets first line and onward
            if i >= 4:
                if x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
                    return True
            # Sixth line crosses first line and onward
            if i >= 5:
                if x[i-2] - x[i-4] >= 0 and x[i] >= x[i-2] - x[i-4] and x[i-1] >= x[i-3] - x[i-5] and x[i-1] <= x[i-3]:
                    return True

        return False

    def isSelfCrossing2(self, x):
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c - e >= 0 and f >= d - b):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False

"""
There are three ways lines would cross itself
                i-2
    case 1 : i-1┌─┐
                └─┼─>i
                 i-3
                 
                    i-2
    case 2 : i-1 ┌────┐
                 └─══>┘i-3
                 i  i-4      (i overlapped i-4)

    case 3 :    i-4
               ┌──┐ 
               │i<┼─┐
            i-3│ i-5│i-1
               └────┘
                i-2
"""
"""
Explanation for Solution 2
            b                              b
   +----------------+             +----------------+
   |                |             |                |
   |                |             |                | a
 c |                |           c |                |
   |                | a           |                |    f
   +----------->    |             |                | <----+
            d       |             |                |      | e
                    |             |                       |
                                  +-----------------------+
                                               d
Draw a line of length a. Then draw further lines of lengths b, c, etc. 
How does the a-line get crossed? From the left by the d-line or from the right by the f-line, 
see the above picture. I just encoded the criteria for actually crossing it.

Two details
1. In both cases, d needs to be at least b. In the first case to cross the a-line directly, 
and in the second case to get behind it so that the f-line can cross it. So I factored out d >= b.
2. The "special case" of the e-line stabbing the a-line from below is covered because 
in that case, the f-line "crosses" it (note that even if there is no actual f-line, 
my code uses f = 0 and thus still finds that "crossing").
"""
x = [2,1,1,2]  # T
# x = [1,2,3,4]  # F
# x = [1,1,1,1]  # T
x = [1,1,2,2,1,1]  # T
print(Solution().isSelfCrossing(x))

