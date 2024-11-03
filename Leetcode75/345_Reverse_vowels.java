class Solution {
    public String reverseVowels(String s) {
        char[] word = s.toCharArray();
        String vowels = "AaEeIiOoUu";
        int start = 0;
        int end = word.length - 1;
        while (start < end) {
            while ((start < end) && (vowels.indexOf(word[start]) == -1)) {
                start++;
            }
            while ((start < end) && (vowels.indexOf(word[end]) == -1)) {
                end--;
            }
            if (start < end) {
                char temp = word[start];
                word[start] = word[end];
                word[end] = temp;
            }
            start++;
            end--;
        }
        return new String(word);
    }
}
