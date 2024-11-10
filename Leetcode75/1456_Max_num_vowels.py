class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiou"
        maxValue = 0
        for i in range(k):
            if s[i] in vowels:
                maxValue += 1

        window = s[:k]
        curValue = maxValue
        for i in range(len(s) - k):
            if s[i] in vowels:
                curValue -= 1
            if s[i+k] in vowels:
                curValue += 1
            if curValue > maxValue:
                maxValue = curValue
        return maxValue
        
