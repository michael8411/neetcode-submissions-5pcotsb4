class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in diffMap:
                return [diffMap[diff], index]
            diffMap[value] = index
            
             
            