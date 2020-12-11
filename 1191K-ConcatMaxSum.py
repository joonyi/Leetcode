"""
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array.
Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.
"""

from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def Kadane(arr, res = 0, cur = 0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res

        mod = 10 ** 9 + 7
        if k > 1:
            return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod
        else:
            return Kadane(arr) % mod

        # return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod if k > 1 else Kadane(arr) % mod


"""

Kadane(arr * 2) is always >= Kadane(arr)
Kadane(arr * 2) will always cross the boundary if sum(arr) > 0
if Kadane(arr * 2) does not cross the boundary, then Kadane(arr * 2) == Kadane(arr)

The maximum SubArray of concatenated_arr can be the sum of all its elements.
For e.g.. if A is {3, 2, -1} and K is 3, then B will be {3, 2, -1, 3, 2, -1, 3, 2, -1}.
The sum of all the elements in concatenated_arr will give us 12. To find this one we don't need to create the array concatenated_arr.
We can simply find the sum of all the elements in array A and we can mutilply it with K.
But wait, we can omit the last term in it so that the sum will become 13.
"""
arr = [1,2]
k = 3
arr = [1,-2,1]
k = 5
print(Solution().kConcatenationMaxSum(arr, k))