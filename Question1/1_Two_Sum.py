import math

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in hashMap:
                return [i, hashMap[complement]]
            else:
                hashMap[nums[i]] = i

        return []
