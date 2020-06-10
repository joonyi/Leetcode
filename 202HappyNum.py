"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:
Input: 19
Output: true

Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
"""
"""
First of all, it is easy to argue that starting from a number I, if some value - say a - appears 
again during the process after k steps, the initial number I cannot be a happy number. 
Because a will continuously become a after every k steps.

Therefore, as long as we can show that there is a loop after running the process continuously, 
the number is not a happy number.
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        store = set()
        while n != 1:
            temp_n = 0
            while n > 0:
                temp_n += (n % 10) ** 2
                n = n // 10
            n = temp_n
            if n in store:
                return False
            else:
                store.add(n)

        return True


n = 49
print(Solution().isHappy(n))