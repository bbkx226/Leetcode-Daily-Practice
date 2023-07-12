// 排序
// Time Complexity: O(n log n)
// Space Complexity: O(log n)

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    // 何为h-index? 有h篇论文分别被引用了至少h次，其余的N-h篇论文被引用次数不超过h次
    // 原理：将论文按被引用次数从大到小排序，如果某篇论文的序号大于等于被引用次数，那么这篇论文就是h-index
    int hIndex(vector<int>& citations) {
        // 从大到小排序
        sort(citations.begin(), citations.end());
        int h = 0, i = citations.size() - 1;
        // 从后往前遍历，直到找到第一个不满足条件的
        while (i >= 0 && citations[i] > h) {
            h++;
            i--;
        }
        return h;
    }
};

int main() {
    Solution sol;
    vector<int> citations = {3, 0, 6, 1, 5};
    cout << sol.hIndex(citations);
    return 0;
}