class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        cleaned = []

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                nums.pop(i)
        return len(nums)
        # curr = nums[0]
        # prev = None
        # for num in nums:
        #     count = 0
        #     curr = num
        #     if curr == prev:
        #         count += 1
        #         nums.remove(curr)
        #     else:
        #         prev = curr
                
        # return len(nums)