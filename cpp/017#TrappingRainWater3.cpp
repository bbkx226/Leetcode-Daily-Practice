// 双指针
// Time Complexity: O(n)
// Space Complexity: O(1)

# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int sum = 0;
        int max_left = 0;
        int max_right = 0;
        int left = 1;
        int right = height.size() - 2;
        // max_left [ i ] 和 max_right [ i ] 数组中的元素我们其实只用一次，然后就再也不会用到了。所以我们可以不用数组，只用一个元素就行了
        
        // if else 条件原理解释：
        // height [ left - 1] 是可能成为 max_left 的变量， 同理，height [ right + 1 ] 是可能成为 right_max 的变量。
        // 只要保证 height [ left - 1 ] < height [ right + 1 ] ，那么 max_left 就一定小于 max_right。
        // 因为 max_left 是由 height [ left - 1] 更新过来的，而 height [ left - 1 ] 是小于 height [ right + 1] 的，而 height [ right + 1 ] 会更新 max_right，所以间接的得出 max_left 一定小于 max_right。

        for (int i = 1; i < height.size() - 1; i++) {
            if (height[left - 1] < height[right + 1]) {
                max_left = max(max_left, height[left - 1]);
                int min_val = max_left;
                if (min_val > height[left]) {
                    sum += (min_val - height[left]);
                }
                left++;
            }
            else {
                max_right = max(max_right, height[right + 1]);
                int min_val = max_right;
                if (min_val > height[right]) {
                    sum += (min_val - height[right]);
                }
                right--;
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