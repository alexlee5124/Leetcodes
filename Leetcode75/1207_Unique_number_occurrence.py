class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        valueMap = {}
        occurrenceMap = {}

        for value in arr:
            if value in valueMap.keys():
                valueMap[value] += 1
            else:
                valueMap[value] = 1

            if valueMap[value] in occurrenceMap.keys():
                occurrenceMap[valueMap[value]] += 1
            else:
                occurrenceMap[valueMap[value]] = 1 
            
            if valueMap[value] > 1:
                occurrenceMap[valueMap[value] - 1] -= 1  
        for value in occurrenceMap.values():
            if value > 1:
                return False
        
        return True
