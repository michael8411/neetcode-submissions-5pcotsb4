from collections import defaultdict


class Solution:
    def groupAnagrams(self, words):
        groups = defaultdict(list)

        for word in words:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())