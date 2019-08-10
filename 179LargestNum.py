"""
Given a list of non negative integers, arrange them such that they form the largest number.
"""
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

    def largestNumber2(self, nums):
        asStrs = list(map(str, nums))
        asStrs.sort(key=LargerNumKey) # compare every pair

        if asStrs[0] == "0":
            return "0"

        largestNumStr = ''
        for s in asStrs:
            largestNumStr += s
        return largestNumStr

nums = [3,30,34,5,9]
print(Solution().largestNumber2(nums))