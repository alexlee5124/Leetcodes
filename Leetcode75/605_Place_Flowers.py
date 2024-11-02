class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i, flower in enumerate(flowerbed):
            if (flower == 0) and (flowerbed[i - 1] == 0 or i == 0) and (flowerbed[i + 1] == 0 or i == len(flowerbed) - 1):
                flowerbed[i] = 1
                n -= 1


        return n <= 0
        
