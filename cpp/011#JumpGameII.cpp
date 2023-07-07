# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

class Solution {
    public:
        int jump(vector<int>& nums)
        {
            // 记录在边界范围内，能跳跃的最远位置的下标
            int ans = 0;
            // 记录当前能跳跃到的位置的边界下标
            int end = 0;
            // 记录在边界范围内，能跳跃的最远位置的下标
            int maxPos = 0;

            // 为什么是nums.size() - 1, 而不是nums.size() ? 因为如果是nums.size()，那么就会多跳一步
            for (int i = 0; i < nums.size() - 1; i++)
            {
                // 继续往下遍历，统计边界范围内，哪一格能跳得更远，每走一步就更新一次能跳跃的最远位置下标
                // 其实就是在统计下一步的最优情况
                maxPos = max(nums[i] + i, maxPos);

                // 当到达数组末端可直接返回
                if(maxPos >= nums.size()-1) return ans+1;

                // 如果到达了边界，那么一定要跳了，下一跳的边界下标就是之前统计的最优情况maxPosition，并且步数加 1
                if (i == end)
                {
                    end = maxPos;
                    ans++;
                }
            }
            return ans;
        }
};

int main()
{
    Solution solution;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << solution.jump(nums) << endl;
    return 0;
}