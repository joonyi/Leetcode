"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according
to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(m):
            for j in range(n):
                if board[i][j].isdigit():
                    if board[i][j] not in rows[i]:
                        rows[i].add(board[i][j])
                    else:
                        return False

                    if board[i][j] not in cols[j]:
                        cols[j].add(board[i][j])
                    else:
                        return False

                    if board[i][j] not in boxes[i // 3][j // 3]:
                        boxes[i // 3][j // 3].add(board[i][j])
                    else:
                        return False

        return True

    def isValidSudoku2(self, board):
        # Go through everything then check for duplicates
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c, j), (i, c), (i // 3, j // 3, c)] # encoded seen as columns, rows, blocks
        return len(seen) == len(set(seen))



board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
] # T
# board = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ] # F
# board = [[".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".","9",".",".",".",".",".",".","1"],
#          ["8",".",".",".",".",".",".",".","."],
#          [".","9","9","3","5","7",".",".","."],
#          [".",".",".",".",".",".",".","4","."],
#          [".",".",".","8",".",".",".",".","."],
#          [".","1",".",".",".",".","4",".","9"],
#          [".",".",".","5",".","4",".",".","."]] # F
print(Solution().isValidSudoku(board))