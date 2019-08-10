"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {"2":'abc', "3":'def', "4":"ghi", "5":"jkl",
                     "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ret = [""] if digits else []

        for d in digits:
            ret = [r+e for e in digit_map[d] for r in ret]
        return ret

    def letterCombinations2(self, digits):
        digit_map = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ret = [""] if digits else []
        for digit in range(len(digits)):
            temp = []
            chars = digit_map[int(digits[digit])]
            for char in range(len(chars)):
                for i in range(len(ret)):
                    temp.append(ret[i] + chars[char])

            ret = temp

        return ret


input = "23"
print(Solution().letterCombinations2(input))