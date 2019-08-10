"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?
"""
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # TLE
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            if i % 2 == 0:
                f[i] = f[i//2] + 1
            else:
                f[i] = min(f[i-1] + 1, f[(i-1)//2 + 1] + 2)

        return f[n]

    def integerReplacement2(self, n):
        # Sample answer
        cnt = 0
        while n > 1:
            cnt += 1
            if n % 2 == 0:
                n >>= 1
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return cnt

    def integerReplacement3(self, n):
        cnt = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                # if n is odd and end with 01 (not 11), n - 1, n = 3 is corner case
                if (n % 2 == 1 and (n >> 1) % 2 == 0) or n == 3:
                    n = n - 1
                else:
                    # two consecutive one, +1, the only exception is when n is 3
                    n = n + 1
            cnt += 1

        return cnt


# n = 6 # expect 3
# n = 15 # 5
n = 6
print(Solution().integerReplacement3(n))