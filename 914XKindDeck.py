"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire
deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
"""

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        import functools
        val = [0] * (max(deck) + 1)
        for card in deck:
            val[card] += 1

        def gcd(a ,b):
            if b == 0:
                return a
            return gcd(b, a%b)

        # return True if functools.reduce(gcd, val) != 1 else False

        # Not using reduce
        res = gcd(val[0], val[0])
        for i in range(1, len(val)):
            res = gcd(res, val[i])
        return res > 1


# deck = [1,2,3,4,4,3,2,1] #T
# deck = [1,1,1,2,2,2,3,3] #F
# deck = [1] #F
# deck = [1,1] #T
# deck = [1,1,2,2,2,2] #T
# deck = [0,0,0,0,0,0
deck = [0,0,0,1,1,1,2,2,2]
print(Solution().hasGroupsSizeX(deck))