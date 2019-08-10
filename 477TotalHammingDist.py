"""
The Hamming distance between two integers is the number of positions at which the
corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.
"""
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TLE. Naive solution
        if len(nums) == 2:
            return self.hammingDistance(nums[0], nums[1])

        dist = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] != nums[j]:
                    dist += self.hammingDistance(nums[i], nums[j])
        return dist

    def hammingDistance(self, x, y):
        z = x ^ y
        res = 0
        while z > 0:
            res += z % 2
            z >>= 1
        return res

    def totalHammingDistance2(self, nums):
        if len(nums) < 2: return 0
        res = 0
        while True:
            zeroOne = [0, 0]
            for i in range(len(nums)):
                zeroOne[nums[i] % 2] += 1
                nums[i] = nums[i] >> 1
            res += zeroOne[0] * zeroOne[1]
            if not any(nums):
                return res

    def totalHammingDistance3(self, nums):
        """
        Total hamming distance for the i-th bit =
        (the number of zeros in the i-th position) *
        (the number of ones in the i-th position).
        """
        bits = [[0, 0] for _ in range(32)]
        for x in nums:
            for i in range(32):
                bits[i][x % 2] += 1
                x //= 2
        return sum(x * y for x, y in bits)

# nums = [4,14,2]
# nums = [1337,7331]
nums = [6,1,8,6,8] # 22
print(Solution().totalHammingDistance3(nums))

"""
The total Hamming distance is constructed bit by bit in this approach.

Let's take a series of number: a1, a2, a3,..., an
Just think about all the Least Significant Bit (LSB) of a(k) (1 ≤ k ≤ n).

How many Hamming distance will they bring to the total?
If a pair of number has same LSB, the total distance will get 0.
If a pair of number has different LSB, the total distance will get 1.

For all number a1, a2, a3,..., a(n), if there are p numbers have 0 as LSB (put in set M), and q numbers have 1 for LSB (put in set N).

There are 2 situations:
Situation 1. If the 2 number in a pair both comes from M (or N), the total will get 0.
Situation 2. If the 1 number in a pair comes from M, the other comes from N, the total will get 1.

Since Situation 1 will add NOTHING to the total, we only need to think about Situation 2

How many pairs are there in Situation 2?
We choose 1 number from M (p possibilities), and 1 number from N (q possibilities).

The total possibilities is p × q = pq, which means
The total Hamming distance will get pq from LSB.

If we remove the LSB of all numbers (right logical shift), the same idea can be used again and again until all numbers becomes zero
"""