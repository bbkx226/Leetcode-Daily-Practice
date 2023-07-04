// 双指针法
# include <vector>
# include <iostream>
using namespace std;

class Solution {
    // 从前往后遍历，将不等于 val 的数放到 nums 的前面
    public:
        // vector 的作用？vector 是一个动态数组，可以根据需要动态扩展
        int removeElement(vector<int>& nums, int val) {
            int n = nums.size();
            int left = 0;
            for (int right = 0; right < n; right++) {
                if (nums[right] != val) {
                    nums[left] = nums[right];
                    left++;
                }
            }
            // 返回 left，即为不等于 val 的元素的个数
            return left;
        }
};

int main() {
    Solution s;
    vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};

    int len = s.removeElement(nums, 2);
    for (int i = 0; i < len; i++) cout << nums[i] << " ";

    cout << endl;
    return 0;
}
