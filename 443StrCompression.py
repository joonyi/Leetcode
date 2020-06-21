"""
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Follow up:
Could you solve it using only O(1) extra space?
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        freq = dict()
        for c in chars:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1

        i = 0
        for key, val in freq.items():
            if val == 1:
                val = ""
            else:
                val = str(val)
            for c in key + val:
                chars[i] = c
                i += 1

        return chars[:i]

    def compress2(self, chars):
        n = len(chars)
        i, count = 0, 1
        for j in range(1, n + 1):
            if j < n and chars[j] == chars[j - 1]:
                count += 1
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    for k in str(count):
                        chars[i] = k
                        i += 1
                count = 1
        chars = chars[:i]
        return i

chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress2(chars))

