"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
         """
        def dfs(board, visited, i, j, word, k, path):
            if path == word:
                return True
            visited[i][j] = True
            for dir in self.directions:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y] \
                        or k >= len(word) or board[x][y] != word[k+1]:
                    continue
                if dfs(board, visited, x, y, word, k+1, path+word[k+1]):
                    return True

            visited[i][j] = False
            return False

        self.directions = ((-1,0),(1,0),(0,-1),(0,1))
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                if board[i][j] == word[0] and dfs(board, visited, i, j, word, 0, word[0]):
                    return True

        return False


# board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
# word = "ABCCED"
# word = "SEE"
# word = "ABCD"
# board = [["a"]]
# word = "b"
board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print(Solution().exist(board, word))