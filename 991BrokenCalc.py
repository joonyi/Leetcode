"""
On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.
"""
class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        # MLE when Y very large
        step = [X - i if i <= X else -1 for i in range(Y + 1)]
        for i in range(X + 1, Y + 1):
            if i % 2 == 0:
                step[i] = step[i//2] + 1
            else:
                step[i] = step[i//2 + 1] + 2
        return step[Y]

    # Start from Y divide to go backward to avoid MLE
    def brokenCalc2(self, X, Y):
        step = 0

        while Y > X:
            if Y % 2 == 1:
                Y += 1
                step += 1
            Y //= 2
            step += 1

        if Y == X:
            return step
        else:
            step += X - Y
            return step

# X = 2
# Y = 3 # expect 2
# X = 5
# Y = 8 # 3
X, Y = 1, 1
# X , Y = 3, 10 # 3
# X , Y = 1024, 1 # 3
# X, Y = 1, 1000000000
print(Solution().brokenCalc2(X, Y))