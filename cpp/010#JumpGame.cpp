// Time Complexity: O(n)    
// Space Complexity: O(1)

# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
    // 为什么能这么做而不需要用动态规划？因为我们只需要知道能不能跳到最后一个位置，而不需要知道怎么跳
    bool canJump(vector<int>& nums) {
        // k 表示能跳到的最远位置
        int k = 0;
        for (int i = 0; i < nums.size(); i++) {
            // 如果当前位置大于能跳到的最远位置，说明跳不到当前位置，直接返回 false
            if (i > k) return false;
            // 更新能跳到的最远位置
            // 每次我都只往右跳一格
            //nums[i]+i 是因为当前的最大覆盖范围等于从当前元素的位置加上当前元素可以跳跃的最大长度，是从i这个位置开始起跳的
            k = max(k, i + nums[i]);
        }
        return true;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << solution.canJump(nums) << endl;
    return 0;
}