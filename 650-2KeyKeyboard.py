"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this
notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number
of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Note:
The n will be in the range [1, 1000].
"""

# The process of making d copies takes d steps (1 step of Copy All and d - 1 steps of Paste)

class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f = [0,0,2,3,4,5,5,7,6]
        s = 0
        for d in range(2,n+1):
            while n % d == 0:
                s += d
                n /= d

        return s

n = 6
print(Solution().minSteps(n))



