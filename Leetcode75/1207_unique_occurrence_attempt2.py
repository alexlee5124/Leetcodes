class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrenceMap = {}
        for num in arr:
            if num in occurrenceMap.keys():
                occurrenceMap[num] += 1
            else:
                occurrenceMap[num] = 1
        
        return len(occurrenceMap.keys()) == len(set(occurrenceMap.values()))
