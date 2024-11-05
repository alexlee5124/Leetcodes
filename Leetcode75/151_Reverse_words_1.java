class Solution {
    public String reverseWords(String s) {
        StringBuilder inputString = new StringBuilder(s);
        inputString = inputString.reverse();
        int left = 0;
        int right = 0;
        int i = 0;
        int n = inputString.length();
        while (i < n) {
            while ((i < n) && (inputString.charAt(i) == ' ')) {
                i++;
            }
            if (i >= n) {
                break;
            }
            while ((i < n) && (inputString.charAt(i) != ' ')) {
                inputString.setCharAt(right++, inputString.charAt(i++));
            }
            StringBuilder temp = new StringBuilder(inputString.substring(left, right)).reverse();
            System.out.println(temp);
            for (int j = 0 ; j < temp.length(); j++) {
                inputString.setCharAt(left, temp.charAt(j));
                left++;
            }
            if (left < n) {
                inputString.setCharAt(left++, ' ');
            }
            right++;
        }
        return inputString.substring(0, right-1).toString();

    }
}
