// 使用额外的数组
// Time Complexity: O(n)
// Space Complexity: O(n)

# include <vector>
# include <iostream>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        // newArr 是一个新的数组，用来存储旋转后的数组
        vector<int> newArr(n);
        for (int i = 0; i < n; ++i) {
            // 使用(i + k) % n 的原因是，当 i + k > n 时，需要从头开始存储
            newArr[(i + k) % n] = nums[i];
        }
        // 将 newArr 中的元素赋值给 nums
        nums.assign(newArr.begin(), newArr.end());
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};

    s.rotate(nums, 3);

    for (int i = 0; i < nums.size(); ++i) {
        cout << nums[i] << " ";
    }

    return 0;
}