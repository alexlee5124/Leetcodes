class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = 0,0
        while (right < len(nums)) and (left<len(nums)):
            while (right < len(nums)) and (nums[right] == 0):
                right += 1
            while (left < len(nums)) and (nums[left] != 0):
                left += 1
            if right >= len(nums) or left >= len(nums):
                break
            if right > left:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
            else:
                right = left
            
