// 双指针
# include <vector>
# include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // p 指向第一个不重复的元素，q 指向下一个元素
        int p=0,q=1;
        // 遍历数组
        while(q < nums.size()) {
            // 如果 nums[p] != nums[q]，将 nums[q] 放到 nums[p+1] 的位置
            if(nums[p]!=nums[q]) {
                // 为何判断 (q - p > 1)？因为如果 q - p = 1，说明 nums[p] != nums[q]，nums[p] 已经在正确的位置上了
                // 因此不需要重新复制，可直接跳过
                if(q - p > 1) nums[p+1]=nums[q];
                p++;
            }
            q++;
        }
        // 返回不重复元素的个数
        return p+1;
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 1, 2, 2, 3, 4, 5, 6};

    int len = s.removeDuplicates(nums);
    for (int i = 0; i < len; i++) cout << nums[i] << " ";

    return 0;
}
