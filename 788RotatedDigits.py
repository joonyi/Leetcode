"""
X is a good number if after rotating each digit individually by 180 degrees, w
e get a valid number that is different from X.  Each digit must be rotated -
we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves;
2 and 5 rotate to each other (on this case they are rotated in a different direction,
in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers
do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?
"""
class Solution:
    def rotatedDigits(self, N: int) -> int:
        counts = 0
        for num in range(1, N + 1):
            number = str(num)
            if '3' in number or '7' in number or '4' in number:  # This will be an invalid number upon rotation
                continue  # Skip this number and go to next iteration
            if '2' in number or '5' in number or '6' in number or '9' in number:
                counts += 1
        return counts

    def rotatedDigits2(self, N):
        # http://www.frankmadrid.com/ALudicFallacy/
        s1 = {0, 1, 8}
        s2 = {0, 1, 8, 2, 5, 6, 9}
        s = set()
        res = 0
        N = list(map(int, str(N)))
        for i, v in enumerate(N):
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    x = 7 ** (len(N) - i - 1)
                    res += 7 ** (len(N) - i - 1) # pick digits from s2 set
                if s.issubset(s1) and j in s1:
                    x = 3 ** (len(N) - i - 1)
                    res -= 3 ** (len(N) - i - 1)  # pick digits from s1 set
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))

    def rotatedDigits3(self, N):
        dp = [0] * (N + 1)
        cnt = 0
        for i in range(N + 1):
            if i < 10:
                if i ==0 or i == 1 or i == 8:
                    dp[i] = 1
                elif i == 2 or i == 5 or i == 6 or i == 9:
                    dp[i] = 2
                    cnt += 1
            else:
                a = dp[i//10]
                b = dp[i % 10]
                if a == 1 and b == 1:
                    dp[i] = 1
                elif a >= 1 and b >= 1:
                    dp[i] = 2
                    cnt += 1
        return cnt



N = 20
print(Solution().rotatedDigits2(N))