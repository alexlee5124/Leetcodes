class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int originalNumber = x;
        int newNumber = 0;
        int remainder = 0;
        while (x > 0) {
            remainder = x % 10;
            newNumber = newNumber * 10 + remainder;
            x = x / 10;
        }
        return (newNumber == originalNumber);
    }
}
