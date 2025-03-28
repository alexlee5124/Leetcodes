class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0, curCount = 0, curNum = nums[0];
        for (int i = 0 ; i < nums.length ; i++) {
            if (nums[i] == curNum) {
                if (curCount == 2) {
                    while (i < nums.length-1 && nums[i+1] == curNum) {
                        i++;
                        curCount++;
                    }
                } else {
                    curCount++;
                    nums[k] = nums[i];
                    k++;
                }
            } else {
                curNum = nums[i];
                curCount = 1;
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
}
