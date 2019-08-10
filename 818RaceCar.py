class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
# Not working
        position, speed = 0, 1
        instr = ''
        while position != target:
            if position < target:
                instr += 'A'
                position += speed
                speed *= 2
            else:
                instr += 'R'
                if speed > 0:
                    speed = -1
                else:
                    position += speed
                    speed = 1

        return len(instr), instr

    def racecar2(self, instr):
        position, speed = 0, 1
        path = []
        for i in instr:
            if i == "A":
                position += speed
                speed *= 2
            else:
                if speed > 0:
                    speed = -1
                else:
                    speed = 1
            path.append(position)
        return path

# target = 4 # expected 5
target = 4
instr = "AARARAAA"
# print(Solution().racecar(target))
print(Solution().racecar2(instr))