def longest_prefix(self, strs):
    if not str:
        return "";
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(longest_prefix(strs))
    