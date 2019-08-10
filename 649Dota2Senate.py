class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate = list(senate)

        ban_R = 0
        ban_D = 0

        while True:
            new_senate = []
            for char in senate:
                if ban_R == 0 and char == "R":
                    new_senate.append("R")
                    ban_D += 1
                elif ban_D == 0 and char == "D":
                    new_senate.append("D")
                    ban_R += 1
                elif ban_R > 0:
                    ban_R -= 1
                elif ban_D > 0:
                    ban_D -= 1

            if new_senate.count("R") == len(new_senate):
                return "Radiant"
            elif new_senate.count("D") == len(new_senate):
                return "Dire"
            else:
                senate = new_senate


senate = "R"
print(Solution().predictPartyVictory(senate))
