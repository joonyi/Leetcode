"""
Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # Brute force TLE
        res = [0] * len(T)
        for i in range(len(T)):
            for j in range(i, len(T)):
                if T[i] < T[j]:
                    res[i] = j - i
                    break

        return res

    def dailyTemperatures2(self, T):
        ans = [0] * len(T)
        stack = []  # last element just enough bigger
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop() # keep pop till just enough bigger
            if stack: # index of element just enough bigger, else remain 0
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans


    # Because temperature in range [30, 100] which is significantly lesse than
    # length of temperature [1, 300000]. Make use of this fact, we store smallest diff appear so far
    # in an array. Index is temperature, val is smallest difference
    def dailyTemperatures3(self, T):
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            # Use 102 so min(nxt[t]) has a default value
            warmer_index = min(nxt[t] for t in range(T[i] + 1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures3(T))