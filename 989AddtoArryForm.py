from math import log10
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A_int = A[0]
        for i in range(1, len(A)):
            A_int = A_int*10 + A[i]

        A_int = A_int + K

        res = [0] * (int(log10(A_int)) + 1)
        i = len(res) - 1
        while A_int > 0:
            res[i] =  A_int % 10
            A_int //= 10
            i -= 1
        return res

    def addToArrayForm2(self, A, K):
        B = []
        while K:
            a = A.pop() if A else 0
            K += a
            K, r = divmod(K, 10)
            B.append(r)
        B.reverse()
        return A + B

A = [1,2,7,0]
K = 34
print(Solution().addToArrayForm2(A, K))