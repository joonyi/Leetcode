"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for n in A:
            if n & 1:
                odd.append(n)
            else:
                even.append(n)
        return even + odd

    def sortArrayByParity2(self, A):
        A.sort(key=lambda x: x % 2)
        return A

    def sortArrayByParity3(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2: # if odd even misplaced
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1 # this number already even
            if A[j] % 2 == 1: j -= 1 # this number already odd

        return A


A = [3,1,2,4]
print(Solution().sortArrayByParity3(A))