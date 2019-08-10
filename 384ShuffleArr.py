"""
Shuffle a set of numbers without duplicates.

Example:
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3]
must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums
        self.res = self.original.copy()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # randomly swap position
        import random
        for i in range(len(self.original)):
            j = random.randint(i, len(self.original)-1)
            self.res[i], self.res[j] = self.res[j], self.res[i]
        return self.res

nums = [1,2,3]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
