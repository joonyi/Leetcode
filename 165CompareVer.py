"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the
fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0.
For example, version number 3.4 has a revision number of 3 and 4 for its first and
second level revision number. Its third and fourth level revision number are both 0.
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        version1 = version1.split(".")
        version2 = version2.split(".")
        for i in range(len(version1)):
            version1[i] = int(version1[i])
        for i in range(len(version2)):
            version2[i] = int(version2[i])

        m, n = len(version1), len(version2)
        if m > n:
            version2 += [0] * (m - n)
        elif m < n:
            version1 += [0] * (n - m)

        for i in range(max(m, n)):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1

        return 0

# version1, version2 = "0.1", "1.1"  # -1
# version1, version2 = "1.0.1", "1"  # 1
# version1, version2 = "7.5.2.4", "7.5.3"  # -1
# version1, version2 = "1.01", "1.001"   # 0
# version1, version2 = "1.0", "1.0.0"  # 0
# version1, version2 = "1.1", "1.10"  # -1
version1, version2 = "1", "1.1"  # -1
# version1, version2 = "1.1", "1.000000000000000000000010"  # -1
# version1 = "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000"
# version2 = "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000"
print(Solution().compareVersion(version1, version2))


