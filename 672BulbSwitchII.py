"""
There is a room with n lights which are turned on initially and 4 buttons on the wall.
After performing exactly m unknown operations towards buttons, you need to return
how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
"""

class Solution(object):
    # TLE
    def flip(self, lights):
        return [light^1 for light in lights]
    def flipEven(self, lights):
        return [light^1 if i % 2 == 0 else light for i, light in enumerate(lights)]
    def flipOdd(self, lights):
        return [light^1 if i % 2 == 1 else light for i, light in enumerate(lights)]
    def flip3k(self, lights):
        return [light^1 if (i) % 3 == 0 else light for i, light in enumerate(lights)]

    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        lights = [1] * n
        queue = [lights]
        operations = [self.flip, self.flipEven, self.flipOdd, self.flip3k]
        for _ in range(m):
            nxt_state = []
            for light in queue:
                for operation in operations:
                    state = operation(light)
                    if state not in nxt_state:
                        nxt_state.append(state)
            queue = nxt_state

        return len(queue)


    def flipLights2(self, n, m):
        n = min(n, 3)
        if m == 0: return 1
        if m == 1: return [2, 3, 4][n - 1]
        if m == 2: return [2, 4, 7][n - 1]
        return [2, 4, 8][n - 1]

    def flipLights3(self, n, m):
        import itertools
        seen = set()
        for cand in itertools.product((0, 1), repeat=4):
            if sum(cand) % 2 == m % 2 and sum(cand) <= m:
                A = []
                for i in range(min(n, 3)):
                    light = 1
                    light ^= cand[0]
                    light ^= cand[1] and i % 2
                    light ^= cand[2] and i % 2 == 0
                    light ^= cand[3] and i % 3 == 0
                    A.append(light)
                seen.add(tuple(A))

        return len(seen)

"""
Suppose we did f[0] of the first operation, f[1] of the second, f[2] of the third, and f[3] of the fourth, where sum(f) == m.

First, all these operations commute: doing operation A followed by operation B yields the same result as doing operation B followed by operation A. Also, doing operation A followed by operation A again is the same as doing nothing. So really, we only needed to know the residues cand[i] = f[i] % 2. There are only 16 different possibilities for the residues in total, so we can try them all.

We'll loop cand through all 16 possibilities (0, 0, 0, 0), (0, 0, 0, 1), ..., (1, 1, 1, 1). A necessary and sufficient condition for cand to be valid is that sum(cand) % 2 == m % 2 and sum(cand) <= m, as only when these conditions are satisfied can we find some f with sum(f) == m and cand[i] = f[i] % 2.

Also, as the sequence of lights definitely repeats every 6 lights, we could replace n with min(n, 6). Actually, we could replace it with min(n, 3), as those lights are representative: that is, knowing the first 3 lights is enough to reconstruct what the next 3 lights will be. If the first 3 lights are X, Y, Z, then with a little effort we can prove the next 3 lights will be (X^Y^Z), Z, Y.
"""
"""
As before, the first 6 lights uniquely determine the rest of the lights. This is because every operation that modifies the xx-th light also modifies the (x+6)(x+6)-th light, so the xx-th light is always equal to the (x+6)(x+6)-th light.

Actually, the first 3 lights uniquely determine the rest of the sequence, as shown by the table below for performing the operations a, b, c, d:

Light 1 = 1 + a + c + d
Light 2 = 1 + a + b
Light 3 = 1 + a + c
Light 4 = 1 + a + b + d
Light 5 = 1 + a + c
Light 6 = 1 + a + b
So that (modulo 2):

Light 4 = (Light 1) + (Light 2) + (Light 3)
Light 5 = Light 3
Light 6 = Light 2
"""
# n = 3
# m = 2
# n = 999
# m = 7
n = 99
m = 1000
print(Solution().flipLights3(n, m))
