"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = ''
        for ad in address:
            if ad != '.':
                res += ad
            else:
                res += '[.]'
        return res

    def defangIPaddr2(self, address):
        return ('[.]'.join(address.split('.')))
        # return address.replace('.', '[.]')

# address = '1.1.1.1'
address = "255.100.50.0"
print(Solution().defangIPaddr(address))
