// 两次遍历
// Time Complexity: O(n)
// Space Complexity: O(n)

# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();

        // 左规则：当 ratings[i−1]<ratings[i]时，i 号学生的糖果数量将比 i−1 号孩子的糖果数量多
        vector<int> left(n);
        for (int i = 0; i < n; i++) {
            // 为何需要判断i>0? 因为left[i] = left[i - 1] + 1; 如果i=0，那么i-1=-1，会越界
            if (i > 0 && ratings[i] > ratings[i - 1]) {
                left[i] = left[i - 1] + 1;
            } else {
                left[i] = 1;
            }
        }
        // 右规则：当 ratings[i]>ratings[i+1]时，i 号学生的糖果数量将比 i+1 号孩子的糖果数量多
        int right = 0, ret = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1 && ratings[i] > ratings[i + 1]) {
                right++;
            } else {
                right = 1;
            }

            ret += max(left[i], right);
        }
        return ret;
    }
};

int main() {
    Solution s;
    vector<int> ratings = {1, 0, 2};
    cout << s.candy(ratings) << endl;
    return 0;
}