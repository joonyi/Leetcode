class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        zeros_ones = [[0,0] for _ in range(len(strs))]
        a, b = 0, 0
        for s in range(len(strs)):
            for char in strs[s]:
                if char == "0":
                    zeros_ones[s][0] += 1
                    a += 1
                else:
                    zeros_ones[s][1] += 1
                    b += 1

        sorted(strs, key=lambda strs: a+b)
        form = [[0 for _ in range(b)] for _ in range(a)]
        for i in range(m):
            for j in range(n):
                for zeros, ones in zeros_ones:
                    if zeros <= i and ones <= j:
                        form[i][j] += 1
                        zeros_ones.remove([zeros,ones])
                        break
                # form[i][j] = max(form[i][j],form[i][j-1])

        return form

    def findMaxForm2(self, strs, m, n):
        # have to go from bottom right to top left why?
        if len(strs) == 0:
            return 0
        dp = [[0 for _ in range(n+1)] for _ in range(m + 1)]
        for s in strs:
            zeros = s.count('0') # num of zeros in this word
            ones = len(s) - zeros   # num of ones in this word
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]



strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
# strs = ["10", "0", "1"]
# m = 1
# n = 1
print(Solution().findMaxForm2(strs, m, n))