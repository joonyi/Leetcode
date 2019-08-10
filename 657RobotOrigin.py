"""
There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move.
Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin
after it finishes all of its moves, return true. Otherwise, return false.
"""
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dir = [0,0]
        for move in moves:
            if move == 'R': dir[0] += 1
            if move == 'L': dir[0] -= 1
            if move == 'U': dir[1] += 1
            if move == 'D': dir[1] -= 1


        if dir[0] or dir[1]:
            return False
        else:
            return True

    def judgeCircle2(self, moves):
         # return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        return not sum(1j ** 'RUL'.find(m) for m in moves) # 1j is complex number

# A = "UD"
A = "LL"
print(Solution().judgeCircle2(A))

