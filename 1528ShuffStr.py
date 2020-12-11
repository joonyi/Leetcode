"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position
moves to indices[i] in the shuffled string.

Return the shuffled string.
"""

from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(indices)
        for i, j in enumerate(indices):
            res[j] = s[i]

        return ''.join(res)



s = "codeleet"
indices = [4,5,6,7,0,2,1,3] # leetcode
# s = "aiohn"
# indices = [3,1,4,2,0] # nihao
# s = "aaiougrt"
# indices = [4,0,2,6,7,3,1,5] # arigatou
print(Solution().restoreString(s, indices))

