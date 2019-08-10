"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have
a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with
index sum 1 (0+1).

Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        least_index_sum = len(list1) + len(list2)
        ret = []
        for i, rest1 in enumerate(list1):
            for j, rest2 in enumerate(list2):
                if rest1 == rest2 and i + j <= least_index_sum:
                    least_index_sum = i + j
                    ret.append(rest2)

        return ret

    def findRestaurant2(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {rest: i for i, rest in enumerate(list1)}
        dict2 = {rest: i for i, rest in enumerate(list2)}
        dictSum = {rest: dict1[rest] + dict2[rest] for rest in dict1 if rest in dict2}
        minSum = min(dictSum.values())
        return [key for key in dictSum if dictSum[key] == minSum]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
print(Solution().findRestaurant(list1, list2))