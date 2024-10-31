class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        i = 0
        while i < len(str1) or i < len(str2):
            if  i < len(str1) and i < len(str2) and str1[i] != str2[i]:
                return ""
            if i == len(str1)-1 and i == len(str2)-1:
                return str1
            if i >= len(str1):
                str2 = str2[i:]
                i = 0
                continue
            if i >= len(str2):
                str1 = str1[i:]
                i = 0
                continue
            i += 1
        
