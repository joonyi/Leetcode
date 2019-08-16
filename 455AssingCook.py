"""
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie. Each child i has a greed factor gi,
which is the minimum size of a cookie that the child will be content with; and each cookie j
has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Assign the cookies starting from the child with less greediness to maximize
        # the number of happy children
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i

# g, s = [1,2,3], [1,1] # 1
# g, s = [1,2], [1,2,3] # 2
g, s = [10,9,8,7], [5,6,7,8] # 2
# g, s = [1,2,3], []
print(Solution().findContentChildren(g, s))