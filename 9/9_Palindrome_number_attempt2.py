class Solution:
    def isPalindrome(self, x: int) -> bool:
        newNumber, quotient, remainder = 0, 1, 0
        originalNumber = x

        while x > 0:
            x, remainder = divmod(x, 10)
            newNumber = newNumber * 10 +  remainder
        return newNumber == originalNumber
