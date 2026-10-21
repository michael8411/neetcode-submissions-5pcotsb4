
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            count = [0] * 26 # a - z

            for char in string:
                position = ord(char) - ord('a')
                count[position] += 1
            key = tuple(count)
            result[key].append(string)
        return list(result.values())
            