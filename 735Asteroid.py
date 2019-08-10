"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one
will explode. If both are the same size, both will explode. Two asteroids moving in the same
direction will never meet.
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i = 0
        while i < len(asteroids) and asteroids[i] < 0:
            stack.append(asteroids[i])
            i += 1

        for asteroid in asteroids[i:]:
            if asteroid > 0:
                stack.append(asteroid)
            elif not stack:
                stack.append(asteroid)
            else: # when asteroid negative
                while stack:
                    if stack[-1] < 0:
                        stack.append(asteroid)
                        break
                    if stack[-1] > abs(asteroid): # [5, 10, -5]
                        break
                    elif stack[-1] == abs(asteroid): # [1,8,-8]
                        stack.pop()
                        break
                    elif stack[-1] < abs(asteroid):
                        stack.pop()
                        if not stack:
                            stack.append(asteroid)
                            break

        return stack

    def asteroidCollision2(self, asteroids):
        stack = []
        i = 0
        while i < len(asteroids):
            if asteroids[i] > 0 or not stack or stack[-1] < 0:
                stack.append(asteroids[i])
            elif stack[-1] <= -asteroids[i]:
                if stack[-1] < -asteroids[i]:
                    i -= 1
                stack.pop()
            i += 1
        return stack

asteroids =  [-2,-2,1,-2]
print(Solution().asteroidCollision2(asteroids))