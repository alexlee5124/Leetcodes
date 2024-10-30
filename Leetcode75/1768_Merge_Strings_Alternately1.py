class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j, k = 0, 0, 0
        finalWord = ""
        while k < len(word1) + len(word2):
            if i >= len(word1):
                finalWord = finalWord + word2[j]
                j = j + 1
            else:
                finalWord = finalWord + word1[i]
                i = i + 1
                if j < len(word2):
                    finalWord = finalWord + word2[j]
                    j = j + 1
            k = i + j
        return finalWord
