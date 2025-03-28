class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            if m == 0:
                nums1 = []
            return
        if m == 0:
            nums1[:] = nums2[:]

        placement = m+n-1
        while placement >= 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[placement] = nums1[m-1]
                m -= 1
                placement -= 1
            else:
                nums1[placement] = nums2[n-1]
                n-= 1
                placement -= 1
            if n == 0:
                nums1[:placement+1] = nums1[:m]
                return
            if m == 0:
                nums1[:placement+1] = nums2[:n]
                return
