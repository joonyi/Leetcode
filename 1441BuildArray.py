"""
Given an array target and an integer n. In each iteration, you will read a number from
list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers
between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.
"""

from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = list(range(1, n + 1))
        stack = []
        i = j = 0
        while i < len(target):
            if target[i] == arr[j]:
                stack.append("Push")
                i += 1
                j += 1
            else:
                while target[i] != arr[j]:
                    stack.append("Push")
                    stack.append("Pop")
                    if target[i] > arr[j]:
                        j += 1
                    else:
                        i += 1

        return stack

    def buildArray2(self, target: List[int], n: int) -> List[str]:
        res = []
        i, j = 1, 0
        while i <= n and j < len(target):
            res.append("Push")
            if target[j] == i:
                j += 1
            else:
                res.append("Pop")
            i += 1
        return res

    def buildArray3(self, target: List[int], n: int) -> List[str]:
        def build():
            curr = 1
            for num in target:
                yield 'Push'
                while curr < num:
                    yield from ('Pop', 'Push')
                    curr += 1
                curr += 1

        return list(build())


# target, n = [1, 3], 3  # ["Push","Push","Pop","Push"]
# target, n = [1,2,3], 3  # ["Push","Push","Push"]
# target, n = [1,2], 4  # ["Push","Push"]
target, n = [2,3,4], 4  # ["Push","Pop","Push","Push","Push"]
print(Solution().buildArray3(target, n))
