class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        mostCandy = max(candies)
        answer = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mostCandy:
                answer.append(True)
            else:
                answer.append(False)
        return answer
