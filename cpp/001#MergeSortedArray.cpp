// 后往前
# include <vector>
# include <algorithm>
# include <iostream>
using namespace std;

class Solution {
    public:
        // 从后往前遍历，将较大的数放到 nums1 的后面
        // 为什么要从后往前遍历？因为 nums1 的后面是空的，从前往后遍历会覆盖 nums1 的元素
        void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
            // i 为 nums1 的最后一个元素的下标
            int i = nums1.size() - 1;
            cout << i << endl;
            m--, n--;
            while (n >= 0) {
                // nums1[m] > nums2[n] 时，将 nums1[m] 与 nums1[i] 交换
                while (m >= 0 && nums1[m] > nums2[n]) {
                    // 交换后，m 和 i 都减 1
                    swap(nums1[i--], nums1[m--]);
                }
                // nums1[m] <= nums2[n] 时，将 nums2[n] 与 nums1[i] 交换
                // 交换后，n 和 i 都减 1
                swap(nums1[i--], nums2[n--]);
            }
        }
};

int main() {
    Solution s;
    vector<int> nums1 = {1, 2, 3, 0, 0, 0}, nums2 = {2, 5, 6};

    s.merge(nums1, 3, nums2, 3);
    for (int i : nums1) cout << i << " ";

    cout << endl;
    return 0;
}
