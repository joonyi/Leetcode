"""
In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or
more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number
we need to buy for each item. The job is to output the lowest price you have to
pay for exactly certain items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents
the price you need to pay for this special offer, other numbers represents how many
specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.
"""
class Solution(object):
    def find_lowest_price(self, price, special, needs):
        # Memorization
        if tuple(needs) in self.dp:
            return self.dp[tuple(needs)]
        # Don't take offers
        cost = 0
        for i, need in enumerate(needs):
            cost += need * price[i]

        # Take one offer
        for offer in special:
            # Make sure it can take at least one offer
            for i, need in enumerate(needs):
                if need < offer[i]:
                    break
            else:
                new_needs = [need - offer[i] for i, need in enumerate(needs)]
                # Update cost
                cost = min(cost, offer[-1] + self.find_lowest_price(price, special, new_needs))
        self.dp[tuple(needs)] = cost
        return cost

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.dp = {}
        return self.find_lowest_price(price, special, needs)

    def shoppingOffers2(self, price, special, needs):
        n = len(price)
        for i in range(n, 6):
            price.append(0)
            needs.append(0)
        for i in range(len(special)-1, -1, -1):
            t = special[i][n]
            special[i][n] = 0
            for j in range(n+1, 7):
                special[i].append(0)
            special[i][6] = t

        dp = [[[[[[[0 for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)]
        m = len(special)
        for j in range(7):
            for k in range(7):
                for p in range(7):
                    for q in range(7):
                        for r in range(7):
                            for s in range(7):
                                dp[j][k][p][q][r][s] = j*price[0]+k*price[1]+p*price[2]+q*price[3]+r*price[4]+s*price[5]

        for i in range(m):
            for j in range(7):
                for k in range(7):
                    for p in range(7):
                        for q in range(7):
                            for r in range(7):
                                for s in range(7):
                                    tt = dp[j - special[i][0]][k - special[i][1]][p - special[i][2]][q - special[i][3]][r - special[i][4]][s - special[i][5]]
                                    dp[j][k][p][q][r][s] = min(dp[j][k][p][q][r][s], tt+ special[i][6])

        return dp[needs[0]][needs[1]][needs[2]][needs[3]][needs[4]][needs[5]]


price, special, needs = [2,5], [[3,0,5],[1,2,10]], [3,2]
print(Solution().shoppingOffers2(price, special, needs))