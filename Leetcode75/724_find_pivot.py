class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rightSum = sum(nums)
        leftSum = 0
        for idx, num in enumerate(nums):
            rightSum -= num
            if leftSum == rightSum:
                return idx
            leftSum += num
        return -1
