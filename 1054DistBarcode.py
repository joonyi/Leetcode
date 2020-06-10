"""
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer,
and it is guaranteed an answer exists.
"""
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        import collections
        i = 0
        res = [0] * len(barcodes)
        for num, freq in collections.Counter(barcodes).most_common():
            for _ in range(freq):
                res[i] = num
                i += 2
                if i >= len(barcodes): i = 1
        return res



# barcodes = [1,1,1,2,2,2]
# barcodes = [1,2,1]
# barcodes = [2,2,1,3]
barcodes = [7,7,7,8,5,7,5,5,5,8]
print(Solution().rearrangeBarcodes2(barcodes))


