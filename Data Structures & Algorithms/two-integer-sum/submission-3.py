from collections import Counter

class Solution(object):
    def twoSum(self, nums, target):
        seen  = {}
        
        for index, number in enumerate(nums):
            diff = target - number

            if diff in seen:
                return [seen[diff], index]
            seen[number] = index