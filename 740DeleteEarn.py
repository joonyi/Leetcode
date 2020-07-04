"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.
"""
from typing import List
import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Not working
        def getScore(num, plusOne, minusOne):
            if plusOne in scores:
                scores.pop(plusOne)
            if minusOne in scores:
                scores.pop(minusOne)
            self.maxScore += num
            if scores[num] == 1:
                scores.pop(num)
            else:
                scores[num] -= 1
            for score in scores:
                getScore(num + score, score - 1, score + 1)

        self.maxScore = 0
        scores = collections.Counter(nums)
        for score in scores:
            getScore(score, score - 1, score + 1)

        return self.maxScore

    def deleteAndEarn2(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0  # avoid and using is numbers pick that is one difference
        for k in sorted(count):
            if k - 1 != prev:  # this new num is not adjacent to prev pick
                # avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
                avoid = max(avoid, using)  # bcs k is not adjacent we can pick avoid or using
                using = k * count[k] + avoid
            else:
                # avoid, using = max(avoid, using), k * count[k] + avoid
                prev_avoid = avoid # bcs k adjacent, can only pick avoid
                avoid = max(avoid, using)
                using = k * count[k] + prev_avoid
            prev = k
        return max(avoid, using)

    def deleteAndEarn3(self, nums):
        """
        This question can be reduced to the 198 House Robbers question
        - The order of nums does not matter
        - Once we decide that we want a num, we can add all the occurrences of num into the total
        nums: [2, 2, 3, 3, 3, 4] (2 appears 2 times, 3 appears 3 times, 4 appears once)
        points: [0, 0, 4, 9, 4] <- This is the gold in each house!
        """
        points, prev, curr = [0] * 10001, 0, 0
        for num in nums:
            points[num] += num
        for value in points:
            # prev, curr = curr, max(prev + value, curr)
            prevprev = prev
            prev = curr
            curr = max(prevprev + value, curr)
        return curr


nums = [3,4,2]  # 6
# nums = [2, 2, 3, 3, 3, 4]  # 9
nums = [3, 1]  # 4
print(Solution().deleteAndEarn2(nums))
