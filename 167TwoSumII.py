"""
Given an array of integers that is already sorted in ascending order, find two numbers such that
they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)
        p, q = 0, len(numbers) - 1
        while p != q:
            if numbers[p] + numbers[q] == target:
                return [p+1, q+1]
            elif numbers[p] + numbers[q] < target:
                p += 1
            else:
                q -= 1

        return []

    # Binary search. Fix first element, binary search on remaining n-1 elements. If cannot find,
    # fix second element, do binary search again. Continue the process till the last element
    # Time complexity is lg(n-1)+lg(n-2)+...+lg(1) = O(lg(n!)) = O(nlgn)
    def twoSum2(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1


numbers, target = [2,7,11,15], 9
print(Solution().twoSum2(numbers, target))