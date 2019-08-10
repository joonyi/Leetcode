"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that
no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
both indicate a queen and an empty space respectively.

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

class Solution(object):
    # This procedure initializes the board to be empty, calls the recursive N-queens
    # procedure and prints the returned solution
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        board = [-1] * n
        self.rQueens(board, 0, [], ret)
        return self.printBoard(ret)

    # This procedure prints the board row by row
    def printBoard(self, board):
        ret = []
        for solution in board:
            temp = []
            for i in solution:
                row = "." * i + 'Q' + '.' * (len(solution) - i - 1)
                temp.append(row)
            ret.append(temp)
        return ret

    # This procedure checks that the most recently placed queen on column current
    # does not conflict with queens in columns to the left.
    def noConflicts(self, board, current):
        for i in range(current):
            if (board[i] == board[current]):
                return False
            if (current - i == abs(board[current] - board[i])):
                return False
        return True

    # This procedure places a queens on the board on a given column so it does
    # not conflict with the existing queens, and then calls itself recursively
    # to place subsequent queens till the requisite number of queens are placed
    def rQueens(self, board, current, path, ret):
        if (current == len(board)):
            ret.append(path)
            return

        for i in range(len(board)):
            board[current] = i
            if (self.noConflicts(board, current)):
                # tmp = "." * len(board)
                # self.rQueens(board, current + 1, path+[tmp[:i]+"Q"+tmp[i+1:]], ret)
                self.rQueens(board, current + 1, path + [i], ret)


print(Solution().solveNQueens(4))


