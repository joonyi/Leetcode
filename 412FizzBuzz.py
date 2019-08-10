"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the
multiples of five output “Buzz”. For numbers which are multiples of both three
and five output “FizzBuzz”.
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [x for x in range(1, n+1)]
        for i, val in enumerate(res):
            if val % 15 == 0:
                res[i] = "FizzBuzz"
            elif val % 3 == 0:
                res[i] = "Fizz"
            elif val % 5 == 0:
                res[i] = "Buzz"
            else:
                res[i] = str(val)

        return res

    def fizzBuzz2(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]

n = 15
print(Solution().fizzBuzz2(n))