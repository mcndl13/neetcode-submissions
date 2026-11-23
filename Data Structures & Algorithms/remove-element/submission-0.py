class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                k += 1
            else:
                nums[idx] = -1

        nums.sort(reverse="True")                
        return k