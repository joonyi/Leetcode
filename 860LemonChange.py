"""
At a lemonade stand, each lemonade costs $5.

Customers are standing in a queue to buy from you, and order one at a time
(in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer, so that the net transaction
is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # Use five, ten, twenty might be better then change
        change = [0, 0, 0]
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                change[0] -= 1
                change[1] += 1
                if change[0] < 0:
                    return False
            elif bill == 20:
                change[2] += 1
                if change[0] >= 1 and change[1] >= 1: # Give out $10 first bcs $5 is basic unit
                    change[0] -= 1
                    change[1] -= 1
                elif change[0] >= 3:
                    change[0] -= 3
                else:
                    return False
        return True



# bills = [5,5,5,10,20] # T
# bills = [5,5,10] # T
# bills = [10, 10] # F
# bills = [5,5,10,10,20] # F
bills = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,10,5,20,20,5,5,5,5,5,10,5,5,5,20,5,5,5,
         10,5,5,10,5,20,5,5,20,5,10,5,5,20,5,5,5,5,5,5,10,20,5,20,20,10,5,20,20,5,10,5,5,5,5,
         5,5,20,20,20,20,5,5,10,5,20,5,5,5,5,10,10,5,5,5,20,5,5,5,5,5,5,20,5,20,10,10,20,5,5,
         5,5,20,20,5,5,5,5,20,5,20,20,5,5,10,5,5,5,20,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,10,
         20,20,5,5,10,20,5,5,5,5,10,20,5,5,10,20,5,10,10,5,5,5,5,5,5,10,10,10,5,10,5,10,5,5,10,
         10,5,5,5,20,5,20,10,20,5,5,5,20,10,5,5,20,5,5,5,10,5,5,10,5,5,20,5,10,10,5,5,10,5,5,10,
         5,10,5,20,10,5,10,10,5,5,5,5,10,5,5,5,20,5,5,5,5,10,5,10,10,5,20,20,5,10,10,10,5,10,5,
         10,5,10,5,5,10,5,5,5,20,5,5,20,5,5,5,5,5,5,10,5,5,20,20,5,5,5,5,10,5,5,5,20,5,5,5,5,10,
         20,5,5,5,20,20,5,10,5,5,5,10,5,10,20,20,5,5,5,5,5,5,20,10,5,10,5,5,20,10,5,5,5,20,5,5,
         5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,10,5,10,5,10,20,10,10,5,5,20,10,20,5,5,5,10,
         5,5,5,10,5,20,20,20,10,20,5,5,5,5,20,5,20,5,10,5,5,5,5,5,5,20,5,10,5,5,5,20,5,5,5,10,
         10,5,5,5,5,5,20,20,20,5,5,5,5,20,5,20,5,20,20,10,10,5,5,5] # T

print(Solution().lemonadeChange(bills))