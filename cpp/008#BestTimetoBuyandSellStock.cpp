// 一次遍历
// Time Complexity: O(n)
// Space Complexity: O(1)

# include <vector>
# include <iostream>
# include <algorithm>
using namespace std;

// 我们只要用一个变量记录一个历史最低价格 minprice，我们就可以假设自己的股票是在那天买的
// 那么我们在第 i 天卖出股票能得到的利润就是 prices[i] - minprice

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int inf = 1e9; // inf = infinity
        int minprice = inf, maxprofit = 0;
        for (int price: prices) {
            maxprofit = max(maxprofit, price - minprice);
            minprice = min(price, minprice);
        }
        return maxprofit;
    }
};

int main() {
    Solution s;
    vector<int> prices = {7, 1, 5, 3, 6, 4};

    cout << s.maxProfit(prices);

    return 0;
}