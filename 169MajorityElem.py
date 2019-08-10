"""
Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""
class Solution(object):
    def majorityElement(self, nums):
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 0
            else:
                dict[num] += 1

            if dict[num] > len(nums)//2:
                return num

        return max(dict, key=dict.get)

    def majorityElement2(self, nums):
        return sorted(nums)[len(nums)//2]

    def majorityElement5(self, nums):
        count = 0
        for i in range(len(nums)):
            if count == 0:
                major = nums[i]
                count = 1
            else:
                if nums[i] == major:
                    count += 1
                else:
                    count -= 1
        return major

"""
Six idea
1. Map each number to its appearance
2. Sort the list and get the n/2-th position element because the definition
The majority element is the element that appears more than n/2 times.
3. Randomization. Random pick an element and see if it is the majority
4. Divide and Conquer. Too complicated
5. Moore's Voting Algorithm. Cancel out each occurrence of an e with all other elements
that are different from e, then e will exist till the end
6. The key lies in how to count the number of 1's on a specific bit. Specifically, 
you need a mask with a 1 on the i-the bit and 0 otherwise to get the i-th bit of each element in nums
"""


input = [1,1,2,3,3,3]
print(Solution().majorityElement2(input))