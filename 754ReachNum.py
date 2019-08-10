"""
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.
"""

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        step = 0
        total = 0
        while total < target:
            step += 1
            total += step
        while (total - target) % 2 != 0:
            step += 1
            total += step
        return step


"""
Step 0: Get positive target value (step to get negative target is the same as to get positive 
value due to symmetry).
Step 1: Find the smallest step that the summation from 1 to step just exceeds or equalstarget.
Step 2: Find the difference between sum and target. The goal is to get rid of the difference to 
reach target. For ith move, if we switch the right move to the left, the change in summation will be 
2*i less. Now the difference between sum and target has to be an even number in order for the math to check out.
Step 2.1: If the difference value is even, we can return the current step.
Step 2.2: If the difference value is odd, we need to increase the step until the difference is even (at most 2 more steps needed).

When the difference is an even value, we will reach the target by switching any right move to the left.
For example, target = 16, we have 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28, we switch 6 to -6, get 16 

"""
target = 16
print(Solution().reachNumber(target))