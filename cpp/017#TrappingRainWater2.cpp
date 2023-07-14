// 动态规划
// Time Complexity: O(n)
// Space Complexity: O(n)

# include <iostream>
# include <vector>
using namespace std;


class Solution {
public:
    int trap(vector<int>& height) {
        int sum = 0;
        // (height.size(), 0) means (size, initial value)
        vector<int> max_left(height.size(), 0);
        vector<int> max_right(height.size(), 0);
        
        // max_left [i] = Max(max_left [i-1],height[i-1])。它前边的墙的左边的最高高度和它前边的墙的高度选一个较大的，就是当前列左边最高的墙了
        for (int i = 1; i < height.size() - 1; i++) {
            max_left[i] = max(max_left[i - 1], height[i - 1]);
        }

        // max_right[i] = Max(max_right[i+1],height[i+1]) 。它后边的墙的右边的最高高度和它后边的墙的高度选一个较大的，就是当前列右边最高的墙了
        for (int i = height.size() - 2; i >= 0; i--) {
            max_right[i] = max(max_right[i + 1], height[i + 1]);
        }

        // 这样，我们再利用解法一的算法，就不用在 for 循环里每次重新遍历一次求 max_left 和 max_right 了。
        for (int i = 1; i < height.size() - 1; i++) {
            int min_val = min(max_left[i], max_right[i]);
            if (min_val > height[i]) {
                sum += (min_val - height[i]);
            }
        }
        return sum;
    }
};

int main() {
    Solution s;
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    cout << s.trap(height) << endl;
    return 0;
}