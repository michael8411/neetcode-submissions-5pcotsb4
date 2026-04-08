class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrayLen = len(nums)
        setLen = len(set(nums))

        return arrayLen != setLen