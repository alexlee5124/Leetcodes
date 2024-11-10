class Solution {
    private static boolean isVowel(char c) {
        if (c == 'a' || c == 'e' ||c == 'i' ||c == 'o' ||c == 'u') {
            return true;
        }
        return false;
    }
    public int maxVowels(String s, int k) {
        int maxValue = 0;
        for (int i = 0 ; i < k ; i ++) {
            if (isVowel(s.charAt(i))) {
                maxValue++;
            }
        }
        int curValue = maxValue;
        for (int i = 0 ; i < s.length() - k ; i ++) {
            if (isVowel(s.charAt(i))) {
                curValue--;
            }
            if (isVowel(s.charAt(i+k))) {
                curValue++;
            }
            if (curValue > maxValue) {
                maxValue = curValue;
            }
        }
        return maxValue;
    }
}
