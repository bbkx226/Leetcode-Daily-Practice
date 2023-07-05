// 贪心算法
// Time Complexity: O(n)
// Space Complexity: O(1)

# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

// 由于不限制交易次数，只要今天股价比昨天高，就交易
// 这道题 「贪心」 的地方在于，对于 「今天的股价 - 昨天的股价」，得到的结果有 3 种可能：
// ① 正数，② 0，③负数。
// 贪心算法的决策是： 只加正数 。
class Solution {
public:
    int maxProfit(vector<int>& prices) {   
        int ans = 0;
        int n = prices.size();
        for (int i = 1; i < n; ++i) {
            ans += max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> prices = {7, 1, 5, 3, 6, 4};

    cout << s.maxProfit(prices);

    return 0;
}