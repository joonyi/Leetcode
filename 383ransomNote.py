"""
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        count = 0
        if len(ransomNote) > len(magazine):
            return False
        else:
            j = 0
            for i in range(len(ransomNote)):
                while j < len(magazine):
                    if ransomNote[i] == magazine[j]:
                        count += 1
                        j += 1
                        break
                    j += 1

            if count == len(ransomNote):
                return True
            else:
                return False

    def canConstruct2(self, ransomNote, magazine):
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

    def canConstruct3(self, ransomNote, magazine):
        m = list(magazine)
        for i in ransomNote:
            if i in m:
                m.remove(i)
            else:
                return False
        return True

print(Solution().canConstruct2("aa", "ab"))