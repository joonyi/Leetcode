class Solution(object):
    def readBinaryWatch(self, n):

        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins > 59: return
            if not n:
                res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
                return
            for i in range(idx, 10): # 10 because 10 LEDs, top 4, bottom 6
                if i < 4:
                    # 1 << i because each button *2
                    dfs(n - 1, hours | (1 << i), mins, i + 1)
                else:
                    # k is num of shift at bottom LEDs
                    k = i - 4
                    dfs(n - 1, hours, mins | (1 << k), i + 1)

        res = []
        dfs(n, 0, 0, 0)
        return res

    def readBinaryWatch2(self, num):
        # Loop through potential value of hour, min
        # if their "1" count in binary form equal num,
        # store the result
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    tmp = '%d:%02d' % (h, m)
                    res.append(tmp)
        return res

num = 2
print(Solution().readBinaryWatch(num))