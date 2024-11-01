class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)

        answer = []
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                answer.append(True)
            else:
                answer.append(False)
        return answer
