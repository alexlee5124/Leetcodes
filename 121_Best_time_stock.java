class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int curMin = prices[0];
        for (int i = 1 ; i < prices.length ; i++) {
            if (prices[i] <= curMin) {
                curMin = prices[i];
            } else {
                if (prices[i] - curMin > profit) {
                    profit = prices[i] - curMin;
                }
            }
        }
        return profit;
    }
}
