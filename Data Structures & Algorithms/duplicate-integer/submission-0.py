class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_map = {}

        for i in range(len(nums)):
            if nums[i] in h_map:
                return True
            h_map[nums[i]] = i
        return False