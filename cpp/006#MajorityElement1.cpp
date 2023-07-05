// HashMap
// Time Complexity: O(n)
// Space Complexity: O(n)
# include <vector>
# include <iostream>
# include <unordered_map>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // unordered_map 是 C++11 新标准中提供的一种用于存储键值对的数据结构，它的底层实现和 map 很类似，都是基于红黑树，但是 unordered_map 的键值对是无序的
        unordered_map<int, int> counts;
        int majority = 0, cnt = 0;
        for (int num: nums) {
            // 何为 ++counts[num]？如果 counts[num] 不存在，会自动创建并初始化为 0，然后再执行 ++ 操作
            ++counts[num];
            if (counts[num] > cnt) {
                // 在遍历数组 nums 时候使用打擂台的方法，维护最大的值，这样省去了最后对哈希映射的遍历
                majority = num;
                cnt = counts[num];
            }
        }
        return majority;
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 2, 2, 2, 3, 4, 5, 6};

    cout << s.majorityElement(nums);

    return 0;
}