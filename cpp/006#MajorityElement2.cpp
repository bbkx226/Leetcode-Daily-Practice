// Sorting 
// Time Complexity: O(log n)
// Space Complexity: O(n log n)
# include <vector>
# include <iostream>
# include <unordered_map>
# include <algorithm>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // sort() 函数默认是升序排序，如果想要降序排序，可以加上第三个参数 greater<int>()
        // begin() 和 end() 函数分别返回指向第一个元素和最后一个元素下一个位置的指针，这两个函数都是 STL 中的函数
        // nums.size() / 2 是因为题目中说了，众数一定存在，所以 nums.size() / 2 一定是众数
        // 何为众数？众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 6, 6, 6};

    cout << s.majorityElement(nums);

    return 0;
}