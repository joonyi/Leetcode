"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
"""
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True

        if A[0] < A[1]:
            incre = 1 # increasing
        elif A[0] > A[1]:
            incre = 0 # decreasing
        else:
            incre = 2 # flat

        i = 0
        while i < len(A)-2:
            i += 1
            if A[i] < A[i+1]:
                if incre == 0:
                    return False
                elif incre == 2:
                    incre = True
            elif A[i] > A[i+1]:
                if incre == 1:
                    return False
                elif incre == 2:
                    incre = False
            else:
                continue

        return True

    def isMonotonic2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n <= 2: return True
        isGreat = False
        isLess = False
        for i in range(1, n):
            if A[i - 1] > A[i]:
                isGreat = True
            if A[i - 1] < A[i]:
                isLess = True

            if isGreat and isLess: # when array is both incre and decre, return False
                return False

        return True

    def isMonotonic3(self, A):
        incre = 1
        decre = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                incre += 1
            elif A[i] < A[i-1]:
                decre += 1
            else:
                incre += 1
                decre += 1
        return incre == len(A) or decre == len(A)

A = [1,2,0]
print(Solution().isMonotonic3(A))