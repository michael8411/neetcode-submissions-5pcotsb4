class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        diffMap = {}
        for i, v in enumerate(numbers):
            diff = target - numbers[i]
            if diff in diffMap:
                return [diffMap[diff] + 1, i+1]
            diffMap[v] = i