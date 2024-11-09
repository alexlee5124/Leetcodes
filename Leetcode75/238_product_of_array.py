class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            elif nums[i] == 0 and zeroCount == 0:
                zeroCount += 1
            else:
                return [0 for j in range(len(nums))]
        answer = []
        for i in range(len(nums)):
            if nums[i] != 0 and zeroCount == 0:
                answer.append(product/nums[i])
            elif nums[i] != 0 and zeroCount == 1:
                answer.append(0)
            else:
                answer.append(product)
        return answer
        
