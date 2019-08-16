"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number,
including the bounds if possible.
"""
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        domain = set([n for n in range(left, right + 1)])
        complement_set = set()
        for p in range(left, right + 1):
            q = p
            while q > 0:
                if q % 10 == 0 or p % (q % 10) != 0:
                    complement_set.add(p)
                    break

                q //= 10

        return sorted(list(domain - complement_set))

    def selfDividingNumbers2(self, left, right):
        res = []
        for i in range(left, right + 1):
            j = i
            while j > 0:
                if j % 10 == 0 or (i % (j % 10)) != 0:
                    break
                j //= 10

            # if j equals zero, the numbers fully divided by itself
            # if j not equals zero, the loop exits early
            if j == 0:
                res.append((i))

        return res

# left, right = 1, 22
left, right = 47, 85

print(Solution().selfDividingNumbers(left, right))
