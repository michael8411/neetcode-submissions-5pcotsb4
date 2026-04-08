class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_map = {}

        for n in nums:
            if n not in dupe_map:
                dupe_map[n] = 1
            else:
                return True
        return False

     
        # arrayLen = len(nums)
        # setLen = len(set(nums))

        # return arrayLen != setLen