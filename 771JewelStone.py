"""
You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.  Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict = {}
        for char in J:
            dict[char] = dict.get(char, 0) + 1
        count = 0
        for char in S:
            if char in dict:
                count += 1
        return count

    def numJewelsInStones2(self, J, S):

        # return sum(map(J.count, S))
        return sum(map(S.count, J)) # both same result

J = "aA"
S = "aAAbbbb"
# J = "z"
# S = "ZZ"
print(Solution().numJewelsInStones2(J, S))