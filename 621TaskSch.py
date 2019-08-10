"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z
where different letters represent different tasks. Tasks could be done without original order.
Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Idea is to sort for most common tasks, then for every loop, execute that task
        char_map = [0] * 26
        for c in tasks:
            char_map[ord(c) - ord("A")] += 1
        char_map.sort()
        time = 0
        while char_map[25] > 0: # while some tasks remain
            i = 0
            while i <= n:
                if char_map[25] == 0:
                    break
                if i < 26 and char_map[25-i] > 0: # if no task, just idle
                    char_map[25-i] -= 1 # execute the task
                time += 1
                i += 1
            char_map.sort()
        return time

    def leastInterval2(self, tasks, n):
        import heapq
        pq = [(-tasks.count(x), x) for x in set(tasks)]
        heapq.heapify(pq)

        time = 0
        while pq:
            i = 0
            tmp = []
            while i <= n:
                if pq:
                    cnt, ch = heapq.heappop(pq)
                    if cnt + 1:
                        tmp.append((cnt+1, ch))

                time += 1
                if not pq and len(tmp) == 0:
                    break

                i += 1
            for task in tmp:
                heapq.heappush(pq, task)

        return time

    def leastInterval3(self, tasks, n):
        char_map = [0] * 26
        for c in tasks:
            char_map[ord(c) - ord("A")] += 1
        char_map.sort()
        max_val = char_map[25] - 1
        idle = max_val * n # Treat all other slots as idle slots

        i = 24
        while i >= 0 and char_map[i] > 0:
            idle -= min(char_map[i], max_val) # reduce idle based on how many tasks filling in
            # idle -= char_map[i] this is wrong bcs can't reduce more than max_val
            i -= 1
        return idle + len(tasks) if idle > 0 else len(tasks)

    def leastInterval4(self, tasks, n):
        import collections
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = list(task_counts).count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)


tasks, n = ["A","A","A","B","B","B"], 2 # Counter example if no sort in while loop
# tasks, n = ["A","A","A","A","A","A","B","C","D"], 2
print(Solution().leastInterval4(tasks, n))