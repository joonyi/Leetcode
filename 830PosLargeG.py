"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions
of every large group.

The final answer should be in lexicographic order.
"""
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        left, right = 0, 1
        while right < len(S):
            while right < len(S) and S[left] == S[right]:
                right += 1

            if right - left >= 3:
                res.append([left ,right-1])

            left = right
            right = left + 1
        return res

# S = "abbxxxxzzy"
# S = "abc"
# S = "abcdddeeeeaabbbcd"
S = 'aa' # []
print(Solution().largeGroupPositions(S))