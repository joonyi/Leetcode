"""
We instead make a clumsy factorial: using the integers in decreasing order,
we swap out the multiply operations for a fixed rotation of operations: multiply (*),
divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
However, these operations are still applied using the usual order of operations
of arithmetic: we do all multiplication and division steps before any addition or subtraction steps,
and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.
This guarantees the result is an integer.

formula: i * (i-1) / (i-2) = i+1 when i >= 5
i * (i-1) / (i-2) + (i-3) - (i-4) * (i-5) / (i-6) + (i-7) - (i-8) * .... + rest elements
=   (i+1) + "(i-3)" - "(i-4) * (i-5) / (i-6)" + "(i-7)" - "(i-8) * " .... + rest elements
=   (i+1) + "(i-3) - (i-3)" + "(i-7) - (i-7)" +  ....  + rest elements
=   (i+1) + rest elements

when 0 element left: final result is (i+1) + ... + 5 - (4*3/2) + 1, which is i+1
when 1 element left: final result is (i+1) + ... + 6 - (5*4/3) + 2 - 1, which is i+2
when 2 element left: final result is (i+1) + ... + 7 - (6*5/4) + 3 - 2 * 1, which is i+2
when 3 element left: final result is (i+1) + ... + 8 - (7*6/5) + 4 - 3 * 2 / 1, which is i-1
"""
class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 2:
            return N
        if N <= 4:
            return N + 3

        if (N - 4) % 4 == 0:
            return N + 1
        elif (N - 4) % 4 <= 2:
            return N + 2
        else:
            return N - 1

    def clumsy2(self, N):
        if N == 0: return 0
        if N == 1: return 1
        if N == 2: return 2
        if N ==3: return 6
        return N  * (N - 1) // (N - 2) + self.rest(N - 3)

    def rest(self, N):
        if N == 0: return 0
        if N == 1: return 1
        if N == 2: return 1
        if N == 3: return 1
        return N - (N - 1) * (N - 2) // (N - 3) + self.rest(N - 4)

N = 12
print(Solution().clumsy2(N))