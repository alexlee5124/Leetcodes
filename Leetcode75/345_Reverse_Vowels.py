class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "AaEeIiOoUu"
        vowelFound = []
        vowelIndexes = []
        for i, char in enumerate(s):
            if char in vowels:
                vowelIndexes.append(i)
                vowelFound.append(char)
        
        s = list(s)
        for i in vowelIndexes:
            s[i] = vowelFound.pop(-1)
        return "".join(s)
        
