"""
Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously.
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        neighbor = [[0 for _ in range(n)] for _ in range(m)]

        if m == 1 and n == 1:
            neighbor[0][0] = 0
        elif m == 1:
            for j in range(n):
                if j == 0 or j == n - 1:
                    neighbor[0][j] = 0
                else:
                    neighbor[0][j] = board[0][j - 1] + board[0][j + 1]
        elif n == 1:
            for i in range(m):
                if i == 0 or i == m - 1:
                    neighbor[i][0] = 0
                else:
                    neighbor[i][0] = board[i - 1][0] + board[i + 1][0]
        else:
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:  # left-top corner
                        neighbor[i][j] = board[i + 1][j] + board[i][j + 1] + board[i + 1][j + 1]
                    elif i == 0 and j == n - 1:  # right-top corner
                        neighbor[i][j] = board[i + 1][j] + board[i][j - 1] + board[i + 1][j - 1]
                    elif i == m - 1 and j == 0:  # left-bot corner
                        neighbor[i][j] = board[i - 1][j] + board[i][j + 1] + board[i - 1][j + 1]
                    elif i == m - 1 and j == n - 1:  # right-bot corner
                        neighbor[i][j] = board[i - 1][j] + board[i][j - 1] + board[i - 1][j - 1]
                    elif i == 0:  # top
                        neighbor[i][j] = board[i + 1][j] + board[i][j - 1] + board[i][j + 1] + board[i + 1][j - 1] + \
                                   board[i + 1][j + 1]
                    elif i == m - 1:  # bot
                        neighbor[i][j] = board[i - 1][j] + board[i][j - 1] + board[i][j + 1] + board[i - 1][j - 1] + \
                                   board[i - 1][j + 1]
                    elif j == 0:  # left
                        neighbor[i][j] = board[i - 1][j] + board[i][j + 1] + board[i + 1][j] + board[i - 1][j + 1] + \
                                   board[i + 1][j + 1]
                    elif j == n - 1:  # right
                        neighbor[i][j] = board[i - 1][j] + board[i][j - 1] + board[i + 1][j] + board[i - 1][j - 1] + \
                                   board[i + 1][j - 1]
                    else:  # 8 neighbours
                        neighbor[i][j] = board[i - 1][j] + board[i][j - 1] + board[i][j + 1] + board[i + 1][j] + \
                                   board[i - 1][j - 1] + board[i - 1][j + 1] + board[i + 1][j - 1] + board[i + 1][j + 1]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:  # living
                    if neighbor[i][j] < 2 or neighbor[i][j] > 3:
                        board[i][j] = 0
                else:  # dead
                    if neighbor[i][j] == 3:
                        board[i][j] = 1



        print(board)
        return

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
board = [[1]]
board = [[1, 1, 1]]
board = [[1],
         [1],
         [1]]
board = [[0,1,0,0,1,1,0],
         [1,1,1,1,1,1,1],
         [1,1,0,0,0,0,1],
         [1,1,0,0,1,0,0]
         ]  # [[1,1,0,0,0,0,1],[0,0,0,1,0,0,1],[0,0,0,0,0,0,1],[1,1,0,0,0,0,0]]
print(Solution().gameOfLife(board))



