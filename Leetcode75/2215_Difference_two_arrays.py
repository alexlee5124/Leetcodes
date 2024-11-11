class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        one = {}
        for num1 in nums1:
            if num1 not in one.keys():
                one[num1] = 1
        two = {}
        oneGhost = []
        for num2 in nums2:
            if num2 in one.keys():
                oneGhost.append(num2)
                del one[num2]
            if num2 not in oneGhost:
                two[num2] = 1

        return [one.keys(), two.keys()]
