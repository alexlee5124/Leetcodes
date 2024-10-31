class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they are both composed of gcd strings
        if (str1 + str2) != (str2 + str1):
            return ""
        from math import gcd
        return str1[:(gcd(len(str1), len(str2)))]
