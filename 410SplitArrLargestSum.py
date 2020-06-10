"""
Given an array which consists of non-negative integers and an integer m, you can split
the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum
among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:
1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
"""
from collections import defaultdict
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if nums == []:
            return 0
        elif m == 1:
            return sum(nums)
        else:
            min_ = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[:j]), self.splitArray(nums[j:], m - 1)
                min_ = min(min_, max(left, right))
            return min_

    # slower memoization
    def splitArray2(self, nums, m):
        cache = defaultdict(dict)
        def recurse(nums, m, i):
            if nums == []:
                return 0
            elif m == 1:
                return sum(nums)
            else:
                if i in cache and m in cache[i]:
                    return cache[i][m]
                cache[i][m] = float('inf')
                for j in range(1, len(nums) + 1):
                    left, right = sum(nums[:j]), recurse(nums[j:], m-1, i+j)
                    cache[i][m] = min(cache[i][m], max(left, right))
                    if left > right:
                        break
                return cache[i][m]

        return recurse(nums, m, 0)

    # Faster memoization
    def helper(self, i, nums, m, cache):
        if i == len(nums):
            return 0
        elif m == 1:
            return sum(nums[i:])
        else:
            if i in cache and m in cache[i]:
                return cache[i][m]
            cache[i][m] = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[i:i + j]), self.helper(i + j, nums, m - 1, cache)
                cache[i][m] = min(cache[i][m], max(left, right))
                if left > right:
                    break
            return cache[i][m]

    def splitArray3(self, nums, m):
        cache = defaultdict(dict)
        return self.helper(0, nums, m, cache)

    def is_valid(self, nums, m, mid):
        # assume mid is < max(nums)
        cuts, curr_sum = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts + 1, x
        subs = cuts + 1
        return (subs <= m)

    def splitArray4(self, nums, m):
        '''
        1. The answer is between sum(array) and max(array)
        2. Binary search for l = max(arr), r = sum(arr)
        3. Use greedy to narrow down left and right boundaries in binary search.
        low, high, ans = max(nums), sum(nums), -1
        3.1 Cut the array from left.
        3.2  Try our best to make sure that the sum of numbers between each two cuts (inclusive) is large enough but still less than mid.
        3.3 We'll end up with two results: either we can divide the array into more than m subarrays or we cannot.
        If we can, it means that the mid value we pick is too small because we've already tried
        our best to make sure each part holds as many non-negative numbers as we can but we still
        have numbers left. So, it is impossible to cut the array into m parts and make sure
        each parts is no larger than mid. We should increase m. This leads to l = mid + 1;
        If we can't, it is either we successfully divide the array into m parts and the sum of
        each part is less than mid, or we used up all numbers before we reach m. Both of them
        mean that we should lower mid because we need to find the minimum one.
        This leads to r = mid - 1;
        '''
        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(nums, m, mid):  # can you make at-most m sub-arrays with maximum sum atmost mid
                ans, high = mid, mid - 1
            else:
                low = mid + 1
        return ans


# There are four ways to split nums into two subarrays. The best way is to split it into
# [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
nums, m = [7,2,5,10,8], 2
nums, m = [5334,6299,4199,9663,8945,3566,9509,3124,6026,6250,7475,5420,9201,9501,38,5897,
           4411,6638,9845,161,9563,8854,3731,5564,5331,4294,3275,1972,1521,2377,3701,6462,
           6778,187,9778,758,550,7510,6225,8691,3666,4622,9722,8011,7247,575,5431,4777,4032,
           8682,5888,8047,3562,9462,6501,7855,505,4675,6973,493,1374,3227,1244,7364,2298,3244,
           8627,5102,6375,8653,1820,3857,7195,7830,4461,7821,5037,2918,4279,2791,1500,9858,
           6915,5156,970,1471,5296,1688,578,7266,4182,1430,4985,5730,7941,3880,607,8776,1348,
           2974,1094,6733,5177,4975,5421,8190,8255,9112,8651,2797,335,8677,3754,893,1818,8479,
           5875,1695,8295,7993,7037,8546,7906,4102,7279,1407,2462,4425,2148,2925,3903,5447,
           5893,3534,3663,8307,8679,8474,1202,3474,2961,1149,7451,4279,7875,5692,6186,8109,
           7763,7798,2250,2969,7974,9781,7741,4914,5446,1861,8914,2544,5683,8952,6745,4870,
           1848,7887,6448,7873,128,3281,794,1965,7036,8094,1211,9450,6981,4244,2418,8610,8681,
           2402,2904,7712,3252,5029,3004,5526,6965,8866,2764,600,631,9075,2631,3411,2737,2328,
           652,494,6556,9391,4517,8934,8892,4561,9331,1386,4636,9627,5435,9272,110,413,9706,5470,
           5008,1706,7045,9648,7505,6968,7509,3120,7869,6776,6434,7994,5441,288,492,1617,3274,
           7019,5575,6664,6056,7069,1996,9581,3103,9266,2554,7471,4251,4320,4749,649,2617,3018,
           4332,415,2243,1924,69,5902,3602,2925,6542,345,4657,9034,8977,6799,8397,1187,3678,4921,
           6518,851,6941,6920,259,4503,2637,7438,3893,5042,8552,6661,5043,9555,9095,4123,142,1446,
           8047,6234,1199,8848,5656,1910,3430,2843,8043,9156,7838,2332,9634,2410,2958,3431,4270,
           1420,4227,7712,6648,1607,1575,3741,1493,7770,3018,5398,6215,8601,6244,7551,2587,2254,
           3607,1147,5184,9173,8680,8610,1597,1763,7914,3441,7006,1318,7044,7267,8206,9684,4814,
           9748,4497,2239], 9
nums, m = [2,3,1,2,4,3], 5
print(Solution().splitArray4(nums, m))
