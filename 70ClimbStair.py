"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# This is fibonacci series because f(n)=f(n-1)+f(n-2)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs2(selfs, n):
        if n == 0:
            return 0
        if n <= 2:
            return n
        f = [0 for i in range(n + 1)]
        f[0], f[1], f[2] = 1, 1, 2
        for i in range(3,n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

    # Same as method 2 but just using int instead of list
    def climbStairs3(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a + b
            a = tmp
        return b

    # using fibonacci formula from wiki
    def climbStairs4(self, n):
        n += 1
        root5 = 5 ** 0.5
        phi = (1 + root5) / 2
        phi2 = (1 - root5) / 2
        return int(1 / root5 * (phi**n - phi2**n))

print(Solution().climbStairs4(3))