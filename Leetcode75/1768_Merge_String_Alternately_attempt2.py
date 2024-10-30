class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        i = 0
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                final = final + word1[i]
            if i < len(word2):
                final = final + word2[i]
            i += 1
        return final
