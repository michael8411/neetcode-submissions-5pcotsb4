class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet, subSet = [], []
        self.helper(0, nums, currSet, subSet)
        return subSet
    
    def helper(self, i, nums, currSet, subSet):
        if i == len(nums):
            subSet.append(currSet.copy())
            return
        
        currSet.append(nums[i])
        self.helper(i + 1, nums, currSet, subSet)
        currSet.pop()
        self.helper(i + 1, nums, currSet, subSet)

