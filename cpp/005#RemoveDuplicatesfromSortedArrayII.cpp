// 双指针
# include <vector>
# include <iostream>
using namespace std;

// 解释原理：
// 前情提要: 有序数组，重复元素最多出现两次
// 1. slow 指向的是下一个不重复元素要放置的位置
// 2. fast 指向的是下一个要处理的元素
// 3. 因为数组是有序的，所以相同元素必然连续
// 4. 如果 nums[slow - 2] != nums[fast]，说明 nums[fast] 是第一次出现，nums[fast] 已经在正确的位置上了
// 5. 如果 nums[slow - 2] == nums[fast]，说明 nums[fast] 是第二次出现，nums[fast] 不应该被保留，需要跳过

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        // 如果数组长度小于等于 2，直接返回数组长度
        if (n <= 2) {
            return n;
        }
        
        int slow = 2, fast = 2;
        while (fast < n) {
            if (nums[slow - 2] != nums[fast]) {
                nums[slow] = nums[fast];
                ++slow;
            }
            ++fast;
        }
        return slow;
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 1, 1, 1, 3, 3, 4, 7};

    int len = s.removeDuplicates(nums);
    for (int i = 0; i < len; i++) cout << nums[i] << " ";

    return 0;
}