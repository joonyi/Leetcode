"""
An encoded string S is given.  To find and write the decoded string to a tape,
the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more
times in total.

Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the
decoded string.
"""

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        tape = []
        for s in S:
            if s.isdigit():
                repeat = int(s) - 1
                tmp = tape[:]
                for _  in range(repeat):
                    tape.extend(tmp)
            else:
                tape.append(s)

            if len(tape) > K:
                return tape[K - 1]

        return tape[K - 1]

    def decodeAtIndex2(self, S, K):
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        # After having total size, search from backwards
        for c in reversed(S):
            K %= size
            # terminate when c pointing at alphabet and at the right position
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size //= int(c)  # reduce length extended by digit
            else:
                size -= 1  # length extended by alpha is one



S = "leet2code3"
K = 10
# S, K = "ha22", 5
# S, K = "a2345678999999999999999", 1
#
# S = "y959q969u3hb22odq595"
# K = 222280369
S = "a23"
K = 6
print(Solution().decodeAtIndex(S, K))