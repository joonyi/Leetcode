"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.
"""
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        count = collections.Counter(words) # return dict with words:frequency
        candidates = list(count.keys())
        candidates.sort(key=lambda w: (-count[w], w)) # w becomes candidates, sort for max then alphabetical order
        return candidates[:k]
        # return [w for w, v in sorted(collections.Counter(words).items(), key = lambda x: (-x[1], x[0])) [:k]]


    def topKFrequent2(self, words, k):
        import collections, heapq
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap) # use priority queue to "sort"
        return [heapq.heappop(heap)[1] for _ in range(k)]


# words, k = ["i", "love", "leetcode", "i", "love", "coding"], 2
words, k = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
print(Solution().topKFrequent2(words, k))