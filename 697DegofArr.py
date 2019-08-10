"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined
as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums,
that has the same degree as nums.
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        d = dict(Counter(nums))
        deg = max(d.values())
        cand = []
        for n, freq in d.items():
            if freq == deg:
                cand.append(n)

        res = []
        for n in cand:
            idx1 = nums.index(n)
            idx2 = len(nums) - nums[::-1].index(n)
            res.append(idx2 - idx1)

        return min(res)

    def findShortestSubArray2(self, nums):
        # Improvement from above is when searching degree, also record left most and right most
        # occurence
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans

    def findShortestSubArray3(self, nums):
        # In one pass, update degree, first encounter of val
        first, counter, res, degree = {}, {}, 0, 0
        for i, v in enumerate(nums):
            first.setdefault(v, i) # first meet this v
            counter[v] = counter.get(v, 0) + 1
            if counter[v] > degree:
                degree = counter[v]
                res = i - first[v] + 1
            elif counter[v] == degree:
                res = min(res, i - first[v] + 1) # compare current idx to first met index
        return res


nums = [1,2,2,3,1]
# nums = [1,2,2,3,1,4,2]
print(Solution().findShortestSubArray3(nums))