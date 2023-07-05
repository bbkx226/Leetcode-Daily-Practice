// 环状替换
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
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        // k 可能大于 n，所以需要取余
        k = k % n;
        // gcd 是最大公约数, 来判断遍历结束
        int count = __gcd(k, n);
        for (int start = 0; start < count; ++start) {
            int current = start;
            int prev = nums[start];
            do {
                // 这里的 next 是下一个要替换的元素的下标
                int next = (current + k) % n;
                swap(nums[next], prev);
                current = next;
                // 如果下一个要替换的元素的下标等于 start，说明已经遍历结束了
            } while (start != current);
        }
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