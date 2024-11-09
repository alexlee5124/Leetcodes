class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        nums = [float(num) / k for num in nums]
        maxValue = sum(nums[0:k])
        curValue = maxValue
        for i in range(len(nums) - k):
            curValue = curValue - nums[i] + nums[i+k]
            if curValue > maxValue:
                maxValue = curValue
        return maxValue
