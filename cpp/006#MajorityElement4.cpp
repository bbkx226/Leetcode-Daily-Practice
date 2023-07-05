// Boyer-Moore 投票算法
// Time Complexity: O(n)
// Space Complexity: O(1)
# include <vector>
# include <iostream>
# include <unordered_map>
# include <algorithm>
using namespace std;

// 解释 Boyer-Moore 投票算法：
// 1. 维护一个候选众数 candidate 和它出现的次数 count。初始时 candidate 可以为任意值，count 为 0；
// 2. 遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count 的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：
// 2.1. 如果 x 与 candidate 相等，那么计数器 count 的值增加 1；
// 2.2. 如果 x 与 candidate 不等，那么计数器 count 的值减少 1。
// 3. 在遍历完成后，candidate 即为整个数组的众数。

// 为何这行得通呢？看看这个算法是怎么消除不同元素之间的配对关系的：
// 1. 首先，考虑最简单的情况，数组中只有一个众数，那么显然地，candidate 会等于这个众数，在遍历过程中，count 会一直等于 1，因为每当遍历到一个新的元素，就会将 count 减少 1，从而抵消掉一个众数和一个非众数。
// 2. 接下来，考虑数组中有两个众数的情况，那么就会有两个不同的候选众数，并且它们会一直坚持到最后留下来的两个候选众数中。这两个候选众数就是这两个众数。count 的计算方式保证了最后两个候选众数不同，因此如果将这两个候选众数返回给数组，必然满足要求。
// 3. 对于其他的情况，如果数组中有超过两个的众数，那么这两个众数就会坚持到最后，并且不同的众数之间进行了配对。同上，count 的计算方式保证了最后留下的两个候选众数是不同的，因此将它们返回到数组中，必然满足要求。

// 一个简单事实：如果一个数组有大于一半的数相同，那么任意删去两个不同的数字，新数组还是会有相同的性质。 基于这个事实，就引发了这个回答一样的相消思想，然后就出来算法了
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = -1;
        int count = 0;
        for (int num : nums) {
            if (num == candidate)
                ++count;
            else if (--count < 0) {
                // 为何这里是 --count 而不是 count--？
                // 因为 --count 是先减后用，而 count-- 是先用后减
                // 如果是 count--，那么在 count 为 0 的时候，会先返回 0，然后再执行 count = 0，这样就不对了; 如果是 --count，那么在 count 为 0 的时候，会先执行 --count = -1，然后再返回 -1，这样就对了
                
                // 我的想法:
                // 由于 众数一定大于一半的数，因此traverse时，非众数和众数相消后，众数的count一定会大于1
                // 例如[1, 2, 2, 2], 1 和 2 相消后，还是会有2，即count=2,而candidate=2 是众数
                candidate = num;
                count = 1;
            }
        }
        return candidate;
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6};

    cout << s.majorityElement(nums);

    return 0;
}