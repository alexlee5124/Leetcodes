class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0, currentStock = prices[0];
        for (int i = 1 ; i < prices.length ; i++) {
            if (prices[i] <= currentStock) {
                currentStock = prices[i];
            } else {
                profit += prices[i] - currentStock;
                currentStock = prices[i];
            }
        }

        return profit;
    }
}
