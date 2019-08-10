"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        # find shortest len so no index out of range error
        lens = [len(str) for str in strs]
        min_len = min(lens)
        result = ''

        for i in range(1, min_len + 1):
            prefix = strs[0][:i]
            for s in strs:
                if s[:i] != prefix:
                    return result
            result = prefix

        return result

    # use zip
    def longestCommonPrefix2(self, strs):
        if len(strs) == 0:
            return ''

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)




strs = ["ABD"]
print(Solution().longestCommonPrefix2(strs))