"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
"""
# Not working
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if all(c != " " and '0' <= c <= '9' for c in s):
            return True

        cnt = 0
        for c in s:
            if "-" or "+":
                cnt += 1
        if cnt == 2:
            return False

A = ["0","0.1","abc","1 a","2e10"," -90e3"," 1e","e3"," 6e-1"," 99e2.5","53.5e93"," --6 ","-+3","95a54e53"]
for a in A:
    print(Solution().isNumber(a))








