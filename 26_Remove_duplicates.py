class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        k = 1
        current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != current:
                nums[k] = nums[i]
                current = nums[i]
                k += 1

        return k
        
        
