"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Surrounded regions shouldn’t be on the border, which means that any 'O' on the
border of the board are not flipped to 'X'. Any 'O' that is not on the border and
it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are
connected if they are adjacent cells connected horizontally or vertically.
"""

# Start from border with 'O', visit all its neighbour and marks '#'
# Visit whole matrix, flip all 'O' to 'X' and flip all '#' back to 'O'
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.visit(board, i, 0)
            if board[i][n-1] == 'O':
                self.visit(board, i, n-1)

        for j in range(n):
            if board[0][j] == 'O':
                self.visit(board, 0, j)
            if board[m-1][j] == 'O':
                self.visit(board, m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

        return board

    def visit(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = '#'
        self.visit(board, i + 1, j)
        self.visit(board, i - 1, j)
        self.visit(board, i, j + 1)
        self.visit(board, i, j - 1)

board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
board2 = [['O','O','X'],['X','X','X']]
board3 = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],
          ["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
print(Solution().solve(board3))