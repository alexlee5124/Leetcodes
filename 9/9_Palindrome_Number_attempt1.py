class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        input = str(x)
        for i in range(len(input)):
            if input[i] != input[-(i+1)]:
                return False

        return True
