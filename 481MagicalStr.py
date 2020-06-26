"""
A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of
characters '1' and '2' generates the string S itself.

The first few elements of string S is the following: S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:
1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:
1 2 2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.
Given an integer N as input, return the number of '1's in the first N number in the magical string S.
Note: N will not exceed 100,000.
"""

class Solution:
    def magicalString(self, n: int) -> int:
        """
        Create an int array a and initialize the first 3 elements with 1, 2, 2.
        Create two pointers head and tail. head points to the number which will be used to generate new numbers. tail points to the next empty position to put the new number. Then keep generating new numbers until tail >= n.
        Need to create the array 1 element more than n to avoid overflow because the last round head might points to a number 2.
        A trick to flip number back and forth between 1 and 2: num = num ^ 3
        """
        if n <= 0: return 0
        if n <= 3: return 1

        s = [0] * (n + 1)
        s[0:2] = [1,2,2]
        head, tail, num, res = 2, 3, 1, 1
        while tail < n:
            for i in range(s[head]):
                s[tail] = num
                if num == 1 and tail < n:
                    res += 1
                tail += 1
            num = num ^ 3  # flip btw 1 and 2
            head += 1
        return res

    def magicalString2(self, n: int) -> int:
        """
        When i is odd, append '1' s[i-1] times, otherwise append '2' s[i-1] times.
        In the end, count how many '1' in S
        """

        s = "122"
        for i in range(3, n + 1):
            if i & 1:
                s += int(s[i-1]) * '1'
            else:
                s += int(s[i-1]) * '2'
        return s[:n].count('1')

# Kolakoski sequence
n = 3  # 1
n = 6  # 3
print(Solution().magicalString(n))