"""
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k), where h is the height of
the person and k is the number of people in front of this person who have a height
greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)

        return queue


# A smallest person is irrelevant for all taller ones. So get tallest person in the queue first,
# and then let smaller person, in descending order, to cut into queue
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(people))

