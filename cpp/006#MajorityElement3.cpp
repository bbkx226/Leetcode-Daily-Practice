// Divide-and-Conquer
// Time Complexity: O(n log n)
// Space Complexity: O(log n)
# include <vector>
# include <iostream>
# include <unordered_map>
# include <algorithm>
using namespace std;

class Solution {
    // 在数组 nums 的区间 [lo, hi] 里统计元素 target 出现的次数
    // 本题中，由于我们要统计的元素 target 一定存在，因此最后一定会返回一个数
    int count_in_range(vector<int>& nums, int target, int lo, int hi) {
        int count = 0;
        for (int i = lo; i <= hi; ++i)
            if (nums[i] == target)
                ++count;
        return count;
    }
    // 分治算法
    int majority_element_rec(vector<int>& nums, int lo, int hi) {
        if (lo == hi)
            return nums[lo];
        int mid = (lo + hi) / 2;
        // 分别找出左右两边的众数
        // 递归的终止条件是区间长度为 1，即 lo == hi
        int left_majority = majority_element_rec(nums, lo, mid);
        int right_majority = majority_element_rec(nums, mid + 1, hi);

        // 如果左右两边的众数相同，那么这个数就是整个区间的众数
        // 否则，比较两个众数在整个区间内出现的次数来决定谁是众数
        // 由于题目中说了，众数一定存在，所以这里不用考虑 lo > hi 的情况
        // > (hi - lo + 1) / 2) 的用处？
        // 如果区间长度是奇数，那么 (hi - lo + 1) / 2 就是区间长度的一半，如果某个数出现的次数大于区间长度的一半，那么它一定是众数
        if (count_in_range(nums, left_majority, lo, hi) > (hi - lo + 1) / 2)
            return left_majority;
        if (count_in_range(nums, right_majority, lo, hi) > (hi - lo + 1) / 2)
            return right_majority;
        return -1;
    }
    public:
        int majorityElement(vector<int>& nums) {
            return majority_element_rec(nums, 0, nums.size() - 1);
        }
};

int main() {
    Solution s;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 6, 6, 6};

    cout << s.majorityElement(nums);

    return 0;
}