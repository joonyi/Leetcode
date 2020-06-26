class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Split the string using '\n' to get all directories and files. For each item, the number of '\t' is how deep the item is.
        maxlen = 0
        pathlen = {0: 0} #represents len of each depth
        input = input.splitlines()
        for line in input:
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1  # +1 for /
        return maxlen

    def lengthLongestPath2(self, input: str) -> int:
        st = [0]  # store path length of each level
        res = 0
        for line in input.splitlines():
            try:
                level = line.rindex("\t") + 1  # ValueError: substring not found
            except:
                level = 0
            length = len(line) - level
            while len(st) > level + 1:
                st.pop()
            if "." in line:
                res = max(res, st[-1] + length)
            else:
                st.append(st[-1] + length + 1)
        return res




input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"  # 20
# input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"  # 32
# input = "dir\n file.txt"  # 9, dir and file.txt in the same depth
print(Solution().lengthLongestPath2(input))
