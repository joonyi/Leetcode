"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import itertools
        res = "1"
        for _ in range(n - 1):
            # s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
            v = []
            # iterate the characters (digits) grouped by digit
            for digit, group in itertools.groupby(res):
                count = len(list(group))
                # v += str(count) + str(digit)
                v.append(str(count))
                v.append(str(digit))
            res = v

        return ''.join(res)

    def countAndSay2(self, n):
        res = '1'
        for _ in range(n - 1):
            char, tmp, count = res[0], [], 0
            for i in res:
                if char == i:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(char)
                    char = i
                    count = 1
            tmp.append(str(count))
            tmp.append(char)
            res = tmp
        return ''.join(res)

n = 5
print(Solution().countAndSay2(n))