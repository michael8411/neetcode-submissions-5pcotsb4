
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            counts = [0] * 26
            for char in string:
                position = ord(char) - ord('a')
                counts[position] += 1
            key = tuple(counts)
            groups[key].append(string)
        return list(groups.values())