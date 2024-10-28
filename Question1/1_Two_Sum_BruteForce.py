class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for idx, num in enumerate(nums):
            for secondIdx, secondNum in enumerate(nums[idx+1:]):
                secondIdx = secondIdx + idx + 1
                if num + secondNum == target:
                    answer = [idx, secondIdx]
                    return answer
