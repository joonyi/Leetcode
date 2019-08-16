"""
Find the minimum length word from a given dictionary words, which has all the
letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still
matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one
that occurs first in the array.

The license plate might have the same letter occurring multiple times.
For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate,
but the word "supper" does.
"""

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        char2prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11,
                      'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
                      'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
                      'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
                      'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97,
                      'z': 101}

        def formatWord(words):
            res = 1
            for letter in words:
                if letter.isalpha():
                    res *= char2prime[letter.lower()]
            return res

        plate2prime = formatWord(licensePlate)
        wordLength = float('inf')
        j = 0
        for i in range(len(words)):
            word2prime = 1
            for w in words[i]:
                word2prime *= char2prime[w]

            if word2prime % plate2prime == 0:
                if len(words[i]) < wordLength:
                    j = i
                    wordLength = len(words[i])

        return words[j]

    def shortestCompletingWord2(self, licensePlate, words):
        import collections
        cntr_lp = {k: v for k, v in collections.Counter(licensePlate.lower()).items() if k.isalpha()}
        res = None
        for word in words:
            check = collections.Counter(word.lower())
            if all(k in check and v <= check[k] for k, v in cntr_lp.items()):
                if not res or len(word) < len(res):
                    res = word
        return res

    # Fastest
    def shortestCompletingWord3(self, licensePlate, words):
        d = {}
        licensePlate = licensePlate.lower()
        for i in licensePlate:
            if i.isalpha():
                d[i] = licensePlate.count(i)
        l = []
        for word in words:
            if all(d[i] <= word.count(i) for i in d.keys()):
                l.append(word)
        return sorted(l, key=len)[0]

licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
# licensePlate = "1s3 456"
# words = ["looks", "pest", "stew", "show"]
print(Solution().shortestCompletingWord3(licensePlate, words))

