class Solution {
    public int majorityElement(int[] nums) {
        int count = 0, candidate = 0;
        for (int i = 0 ; i < nums.length ; i++) {
            if (count == 0) {
                candidate = nums[i];
                count++;
            } else if (candidate == nums[i]) {
                count++;
            } else if (candidate != nums[i]) {
                count--;
            }
        }
        return candidate;
    }
}
