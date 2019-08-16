"""
Given an integer array with even length, where different numbers in this array represent
different kinds of candies. Each number means one candy of the corresponding kind.
You need to distribute these candies equally in number to brother and sister.
Return the maximum number of kinds of candies the sister could gain.
"""
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        d = {}
        for candy in candies:
            if candy in d:
                d[candy] += 1
            else:
                d[candy] = 1

        if len(d) > len(candies) // 2:
            return len(candies) // 2
        else:
            return len(d)

    def distributeCandies2(self, candies):
        S = set(candies)
        return len(candies) // 2 if len(S) > len(candies) // 2 else len(S)

# candies = [1,1,2,2,3,3]
candies = [1,1,2,3]
print(Solution().distributeCandies2(candies))