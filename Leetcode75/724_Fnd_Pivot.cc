class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int rightSum = 0, leftSum = 0;
        for (int i = 0 ; i < nums.size() ; i++) {
            rightSum += nums[i];
        }
        if ((rightSum -= nums[0]) == leftSum) {
            return 0;
        }
        for (int i = 1 ; i < nums.size() ; i++) {
            rightSum -= nums[i];
            leftSum += nums[i-1];
            if (rightSum == leftSum) {
                return i;
            }
        }
        return -1;
    }
};
