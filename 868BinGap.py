"""
Given a positive integer N, find and return the longest distance between
two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.
"""
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N & (N - 1) == 0:
            return 0

        cnt = 0
        longest = 0
        while N > 0:
            if N % 2 == 1:
                cnt = 1
            else:
                cnt = cnt + 1 if cnt != 0 else 0
            longest = max(longest, cnt)
            N >>= 1

        return longest

    def binaryGap2(self, N):
        last = None
        ans = 0
        for i in range(32):
            if (N >> i) & 1: # extract LSB
                if last is not None: # avoid wrong ans with only one 1
                    ans = max(ans, i - last)
                last = i
        return ans



N = 22 # 2
# N = 5 # 2
# N = 6 # 1
# N = 8 # 0
print(Solution().binaryGap2(N))