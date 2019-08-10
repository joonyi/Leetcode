"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine,
'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has
no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents
how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
return the board after revealing this position according to the following rules:

1. If a mine ('M') is revealed, then the game is over - change it to 'X'.
2. If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B')
and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square ('E') with at least one adjacent mine is revealed, then change it to a
digit ('1' to '8') representing the number of adjacent mines.

Return the board when no more squares will be revealed.
"""

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m = len(board)
        n = len(board[0])
        row = click[0]
        col = click[1]

        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            count = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if i == 0 and j == 0:
                        continue
                    r = row + i
                    c = col + j
                    if r < 0 or r >= m or c < 0 or c >= n:
                        continue
                    if board[r][c] == 'M' or board[r][c] == 'X':
                        count += 1

            if count > 0:
                board[row][col] = str(count)
            else:
                board[row][col] = 'B'
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i == 0 and j == 0:
                            continue
                        r = row + i
                        c = col + j
                        if r < 0 or r >= m or c < 0 or c >= n:
                            continue
                        if board[r][c] == 'E':
                            self.updateBoard(board,[r,c])
        return board

input = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
#[['B', '1', 'E', '1', 'B'],['B', '1', 'M', '1', 'B'],['B', '1', '1', '1', 'B'],['B', 'B', 'B', 'B', 'B']]
click = [3,0]
print(Solution().updateBoard(input,click))

