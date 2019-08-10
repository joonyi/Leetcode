"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of
those people is at most limit.

Return the minimum number of boats to carry every given person.
(It is guaranteed each person can be carried by a boat.)
"""

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # Time Limit Exceeded
        num = 0
        i = 0
        while any(people):
            while not people[i]:
                i += 1

            boat = people[i]
            people[i] = 0
            left = limit - boat

            nxt = 0
            nxt_max = 0
            j = i + 1
            while j < len(people):
                if people[j] == left:
                    nxt_max = people[j]
                    nxt = j
                    break
                elif nxt_max < people[j] < left:
                    nxt_max = people[j]
                    nxt = j
                j += 1
            # if nxt_max != 0:
            people[nxt] = 0

            num += 1
            i += 1

        return num
    """
    If the heaviest person can share a boat with the lightest person, then do so. 
    Otherwise, the heaviest person can't pair with anyone, so they get their own boat.
    
    The reason this works is because if the lightest person can pair with anyone, 
    they might as well pair with the heaviest person.
    """
    def numRescueBoats2(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans

# people = [3,5,3,4] # expect 4
# limit = 5
# people = [5,1,4,2] # 2
# limit = 6
# people = [2,2] # 1
# limit = 6
# people = [1,5,3,5] # 3
# limit = 7
# people = [3,8,7,1,4] # 3
# limit = 9
# people = [1,2] # 1
# limit = 3
people = [21,40,16,24,30] # expect 3
limit = 50
print(Solution().numRescueBoats2(people, limit))