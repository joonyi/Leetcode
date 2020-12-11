"""
Given a positive integer K, you need find the smallest positive integer N such that
N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.
"""


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remain = 1
        N = 1
        cnt = 1
        seen = set()
        while remain % K != 0:
            N = N * 10 + 1
            remain = N % K
            cnt += 1

            if remain in seen :
                return -1
            else:
                seen.add(remain)

        return cnt

    def smallestRepunitDivByK2(self, K: int) -> int:
        remainder = 0
        for length_N in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return length_N
        return -1


"""
For a given K, we evaluate 1 % K, 11 % K, 111 % K, ..., 11...1 (K '1's) % K.

If any remainder is 0, then the current number is the smallest integer divisible by K.
If none of the remainders is 0, then at some point, there must be some duplicate remainders 
(due to Pigeonhole principle), as the K remainders can only take at most K-1 different values 
excluding 0. In this case, no number with the pattern 1...1 is divisible by K. 
This is because once a remainder has a duplicate, the next remainder will be in a loop, 
as the previous remainder determines the next_mod, i.e., next_mod = (10 * prev_mod + 1) % K. 
Therefore, we will never see remainder==0.

"""
N = 3
N = 1
N = 2
# N = 17
print(Solution().smallestRepunitDivByK2(N))