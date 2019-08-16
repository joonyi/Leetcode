"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops,
and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively.
Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions
(north, east, west, and south), then moves in that direction until it chooses to stop,
reaches the edge of the board, or captures an opposite colored pawn by moving to the same square
it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        rook = [0,0]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    rook = [i,j]
                    break

        cnt = 0
        i, j = rook
        while i > 0:
            if board[i - 1][j] == 'p':
                cnt += 1
                break
            elif board[i - 1][j] == 'B':
                break
            i -= 1

        i, j = rook
        while i < m - 1:
            if board[i + 1][j] == 'p':
                cnt += 1
                break
            elif board[i + 1][j] == 'B':
                break
            i += 1

        i, j = rook
        while j > 0:
            if board[i][j - 1] == 'p':
                cnt += 1
                break
            elif board[i][j - 1] == 'B':
                break
            j -= 1

        i, j = rook
        while j < n - 1:
            if board[i][j + 1] == 'p':
                cnt += 1
                break
            elif board[i][j + 1] == 'B':
                break
            j += 1

        return cnt

# board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","R",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(Solution().numRookCaptures(board))