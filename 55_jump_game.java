class Solution {
    public boolean canJump(int[] nums) {
        int potential = 1;
        for (int i = 0 ; i < nums.length ; i++) {
            potential--;
            if (potential < 0) {
                return false;
            }
            if (nums[i] > potential) {
                potential = nums[i];
            }
        }
        return true;
    }
}
