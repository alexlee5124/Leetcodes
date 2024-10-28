class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;
        int complement;
        for (int i = 0 ; i < n ; i++) {
            complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[]{numMap.get(complement), i};
            }
            else {
                numMap.put(nums[i], i);
            }
        }     
        return new int[]{};
    }
}
