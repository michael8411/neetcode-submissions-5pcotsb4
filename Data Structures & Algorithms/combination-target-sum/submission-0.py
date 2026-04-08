class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        currSet, subSet = [], []
        self.helper(0, nums, currSet, subSet, target)
        return subSet

    def helper(self, i, nums, currSet, subSet, target):
        if target == 0:
            subSet.append(currSet.copy())
            return

        if i == len(nums):
            return
        
        if  target >= nums[i] :
            currSet.append(nums[i])

            self.helper(i, nums, currSet, subSet, target - nums[i])
            currSet.pop()
        self.helper(i+1, nums, currSet, subSet, target)            