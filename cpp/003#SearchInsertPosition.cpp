// 二分查找
# include <vector>
# include <iostream>
using namespace std;

class Solution {
    public:
        int searchInsert(vector<int>& nums, int target) {
            int left = 0, right = nums.size() - 1;
            // 当 left == right 时，区间 [left, right] 依然有效
            // 为什么使用 <= 而不是 < ？因为初始化 right = nums.size() - 1, 因此决定了搜索区间是 [left, right]
            while(left<=right){
                int mid = (left + right) / 2; // int mid = (left + right) >> 1;
                if(nums[mid] == target) return mid;
                else if(nums[mid] < target) left = mid + 1;
                else right = mid - 1;
            }
            return left;
        }
};

int main() {
    Solution s;
    vector<int> nums = {1, 3, 4, 6};

    cout << s.searchInsert(nums, 5) << endl;

    return 0;
}