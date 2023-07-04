// 双指针法优化
# include <vector>
# include <iostream>
using namespace std;

class Solution {
public:
    // 双指针法优化，优化了什么？ 
    // 1. 将不等于 val 的数放到 nums 的前面，不需要将等于 val 的数放到 nums 的后面
    // 3. 不需要遍历完 nums，只需要遍历到 left
    int removeElement(vector<int>& nums, int val) {
        // left 指向第一个不等于 val 的元素, right 指向最后一个不等于 val 的元素
        int left = 0, right = nums.size();
        // 当左指针 left 与右指针 right 重合时，遍历结束
        while (left < right) {
            // 如果 nums[left] == val，将 nums[left] 与 nums[right - 1] 交换
            if (nums[left] == val) {
                nums[left] = nums[right - 1];
                right--;
            
            } else {
                left++;
            }
        }
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
