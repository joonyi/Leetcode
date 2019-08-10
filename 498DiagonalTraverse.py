"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the
matrix in diagonal order as shown in the below image.
"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return matrix
        m, n = len(matrix), len(matrix[0])
        def traverse(matrix, i, j, up): # up 1, down 0
            self.res.append(matrix[i][j])
            if i == m - 1 and j == n - 1:
                return
            if up:
                if 0 <= i - 1 and j + 1 < n:
                    traverse(matrix, i - 1, j + 1, 1)
                elif j + 1 < n:
                    traverse(matrix, i, j + 1, 0)
                else:
                    traverse(matrix, i + 1, j, 0)
            else:
                if i + 1 < m and 0 <= j - 1:
                    traverse(matrix, i + 1, j - 1, 0)
                elif i + 1 < m:
                    traverse(matrix, i + 1, j, 1)
                else:
                    traverse(matrix, i, j + 1, 1)

        self.res = []
        traverse(matrix, 0, 0, 1)
        return self.res

    def findDiagonalOrder2(self, matrix):
        if not matrix: return matrix
        r, c = 0, 0
        m, n  = len(matrix), len(matrix[0])
        A = [0] * (m * n)
        for i in range(len(A)):
            A[i] = matrix[r][c]
            if (r + c) % 2 == 0: # if even sum moving up
                if c == n - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return A



    def findDiagonalOrder3(self, matrix):
        # Assemble all the diagonal into a deque then merge them
        from collections import deque, defaultdict
        if matrix == []:
            return []
        M, N = len(matrix), len(matrix[0])
        result = defaultdict(deque)
        max_sum, top_down = M + N - 2, True
        for i in range(M):
            for j in range(N):
                s = i + j
                if s & 1:
                    result[s].append(matrix[i][j])
                else:
                    result[s].appendleft(matrix[i][j])
        output = []
        for s in range(max_sum + 1):
            output.extend(result[s])
        return output


# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
matrix = [[2,5],[8,4],[0,-1]]
print(Solution().findDiagonalOrder3(matrix))