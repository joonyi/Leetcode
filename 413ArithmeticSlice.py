"""
A sequence of number is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        f = [0] * len(A)
        sum = 0
        for i in range(2, len(f)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                f[i] = 1 + f[i - 1]
                sum += f[i]

        return sum

    def numberOfArithmeticSlices2(self, A):
        # can simply track how many consecutive arithmetic sequence slice
        count = 0
        sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count = 1 + count
                sum += count
            else:
                count = 0
        return sum

    def numberOfArithmeticSlices3(self, A):
        count = 0
        sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count += 1
            else:
                sum += count * (count + 1) // 2
                count = 0
        sum += count * (count + 1) // 2
        return sum

A = [1,2,3,4,5,6] # expect 10
# A = [1,2,3,4] # expect 3
# A = [1,2,3,8,9,10] # expect 2
print(Solution().numberOfArithmeticSlices(A))