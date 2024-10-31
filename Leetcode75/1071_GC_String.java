class Solution {
    public int GCD(int n1, int n2) {
        if (n2 == 0) {
            return n1;
        }
        return GCD(n2, n1 % n2);
    }
    public String gcdOfStrings(String str1, String str2) {
        // See if they are composed of the same gcd block
        if (!(str1+str2).equals(str2+str1)) {
            return new String("");
        }
        
        return str1.substring(0, GCD(str1.length(), str2.length()));
    }
}
