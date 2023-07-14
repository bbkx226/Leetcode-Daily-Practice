// 按列求
// Time Complexity: O(n^2)
// Space Complexity: O(1)

# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int sum = 0;
        //最两端的列不用考虑，因为一定不会有水。所以下标从 1 到 length - 2
        for (int i = 1; i < height.size() - 1; i++) {

            int max_left = 0;
            //找出左边最高
            for (int j = i - 1; j >= 0; j--) {
                if (height[j] > max_left) {
                    max_left = height[j];
                }
            }

            int max_right = 0;
            //找出右边最高
            for (int j = i + 1; j < height.size(); j++) {
                if (height[j] > max_right) {
                    max_right = height[j];
                }
            }

            //找出两端较小的
            int min_val = min(max_left, max_right);
            
            //只有较小的一段大于当前列的高度才会有水，其他情况不会有水
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