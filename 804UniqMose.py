"""
International Morse Code defines a standard encoding where each letter is mapped to a series of
dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-").
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
"""
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = {'a':".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
                 'f': "..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---",
                 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---",
                 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-",
                 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--",
                 'z':"--.."
                 }

        transform = set()
        for word in words:
            res = ''
            for ch in word:
                res += morse[ch]
            transform.add(res)

        return len(transform)

    def uniqueMorseRepresentations2(self, words):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                 ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transform = set()
        for word in words:
            res = ''
            for ch in word:
                res += morse[ord(ch) - ord('a')]
            transform.add(res)
        return len(transform)

words = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations2(words))