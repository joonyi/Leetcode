"""
Given two strings a and b, find the length of the longest uncommon subsequence between them.

A subsequence of a string s is a string that can be obtained after deleting any number of
characters from s. For example, "abc" is a subsequence of "aebdc" because you can delete the
underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include
"aebdc", "aeb", and "" (empty string).

An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.

Return the length of the longest uncommon subsequence between a and b. If the
longest uncommon subsequence doesn't exist, return -1.
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        return max(len(a), len(b))


"""
These three cases are possible with string a and b:

1. a==b 
If both the strings are identical, it is obvious that no subsequence will be uncommon. 
Hence, return -1.

2. len(a)==len(b) and a != b 
Example: abc, abd. In this case we can consider any string i.e. abc or abd as a required subsequence, 
as out of these two strings one string will never be a subsequence of other string. 
Hence, return length(a)length(a) or length(b)length(b).

3. len(a) != len(b) 
Example abcd, abc. In this case we can consider bigger string as a required subsequence 
because bigger string can't be a subsequence of smaller string. 
Hence, return max(len(a),len(b))

"""

a, b = "aba", "cdc"  # 3
# a, b = "aaa", "bbb" # 3
# a, b = "aaa", "aaa" # -1

print(Solution().findLUSlength(a, b))