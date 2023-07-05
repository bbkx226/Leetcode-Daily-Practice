// 动态规划
// Time Complexity: O(n)
// Space Complexity: O(n)

# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int dp[n][2];
        // 初始化
        dp[0][0] = 0, dp[0][1] = -prices[0];
        
        for (int i = 1; i < n; ++i) {
            // dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润
            // dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润
            // dp[i][0] = max(前一天没有股票的最大利润, 前一天有股票的最大利润 + 今天卖出股票)
            // dp[i][1] = max(前一天有股票的最大利润, 前一天没有股票的最大利润 - 今天买入股票)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        }
        return dp[n - 1][0];
    }
};

int main() {
    Solution s;
    vector<int> prices = {7, 1, 5, 3, 6, 4};

    cout << s.maxProfit(prices);

    return 0;
}