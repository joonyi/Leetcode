"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import bisect
        # Although the elements are not correct, but the length is correct
        a = []
        for num in nums:
            i = bisect.bisect_left(a, num)  # the return index partition left < num, right >= num
            if i == len(a):  # new index bigger than the rightmost num
                a.append(num)
            else:
                a[i] = num  # element has been changed, but the sub's length has not changed.

            if len(a) == 3:
                return True

        return False

    def increasingTriplet2(self, nums):
        small = float('inf')
        big = float('inf')
        for n in nums:
            if n <= small:
                small = n
            elif n <= big:  # big only gets updated when there exists a small that comes before it
                big = n
            else:
                return True
        return False



# nums = [1,2,3,4,5]
nums =[5,4,3,2,1]
# nums = [2,4,-2,-3]
nums = [1, 3, 0, 5]
nums = [8,7,6,7,5,8]
print(Solution().increasingTriplet2(nums))