class Solution {
    public int maxProfit(int[] prices) {
        int min_price = prices[0];
        int max_profit = 0;
        for (int i = 0; i < prices.length; i++) {
            int c_profit = prices[i] - min_price;
            if (prices[i] < min_price) {
                min_price = prices[i];
            }

            if (c_profit >= max_profit) {
                max_profit = c_profit;
            }
        }
        return max_profit;
    }
}
