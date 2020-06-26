"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7,
write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().
"""
import random
def rand7():
    return random.randint(1, 7)

class Solution:
    def rand10(self):
        # Rejection Sampling
        # The main idea is when you generate a number in the desired range,
        # output that number immediately. If the number is out of the desired range,
        # reject it and re-sample again.
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1  # rand 0 ~ 48 but reject 40 ~ 48
        return rand40 % 10 + 1  # 0 ~ 39 and %10 + 1 become 1 ~ 10

    def rand102(self):
        mp = {(1, 1): 1,
              (1, 2): 2,
              (1, 3): 3,
              (1, 4): 4,
              (1, 5): 5,
              (1, 6): 6,
              (1, 7): 7,
              (2, 1): 8,
              (2, 2): 9,
              (2, 3): 10}
        while True:
            x = rand7()
            y = rand7()
            if (x, y) in mp:
                return mp[(x, y)]


print(Solution().rand10())