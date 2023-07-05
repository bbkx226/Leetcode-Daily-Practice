// 数组翻转
// Time Complexity: O(n)
// Space Complexity: O(1)

# include <vector>
# include <iostream>
# include <cstdio>
# include <algorithm>
# include <numeric>
using namespace std;

class Solution {
    public:
        void reverse(vector<int>& nums, int start, int end) {
            while (start < end) {
                swap(nums[start], nums[end]);
                start += 1;
                end -= 1;
            }
        }

        void rotate(vector<int>& nums, int k) {
            k %= nums.size();
            // 先将整个数组翻转
            reverse(nums, 0, nums.size() - 1);
            // 再将前 k 个元素翻转
            reverse(nums, 0, k - 1);
            // 最后将后 n - k 个元素翻转
            reverse(nums, k, nums.size() - 1);
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