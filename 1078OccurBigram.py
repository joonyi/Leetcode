"""
Given words first and second, consider occurrences in some text of the form "first second third",
where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.
"""

from typing import List
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        """"""
        res = []
        text = text.split()
        for i in range(len(text) - 1):
            if text[i] == first and text[i + 1] == second and i + 2 < len(text):
                res.append(text[i + 2])
        return res

    def findOcurrences2(self, text, first, second):
        """
        s0 initial state
        s1 detected first, waiting for second to come
        s2 detected second after detecting first, aka. the accepting state
        """
        array = text.split(" ")  # split words
        state = 0  # current state
        res = []  # results

        for i, v in enumerate(array):
            if state == 0:  # current state is 0
                if v == first:  # input is first
                    state = 1  # switch to state 1
                else:
                    state = 0  # else remain state 0
            elif state == 1:
                if v == second:
                    state = 2  # enter the accepting state
                    try:
                        res.append(array[i + 1])  # put the word that comes after this word into results
                    except:
                        pass
                elif v == first:
                    state = 1
                else:
                    state = 0
            elif state == 2:
                if v == first:
                    state = 1
                else:
                    state = 0

        return res

text = "alice is a good girl she is a good student"
first = "a"
second = "good"
# text = "we will we will rock you"
# first = "we"
# second = "will"
print(Solution().findOcurrences2(text, first, second))
