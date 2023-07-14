// 纵向扫描
// Time Complexity: O(m*n)
// Space Complexity: O(1)

# include <iostream>
# include <vector>
# include <string>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (!strs.size()) {
            return "";
        }
        // 以第一个字符串为基准
        int length = strs[0].size();
        // 字符串个数
        int count = strs.size();
        for (int i = 0; i < length; ++i) {
            char c = strs[0][i];
            for (int j = 1; j < count; ++j) {
                // 如果当前字符不相等或者已经到达某个字符串的末尾
                if (i == strs[j].size() || strs[j][i] != c) {
                    return strs[0].substr(0, i);
                }
            }
        }
        return strs[0];
    }
};

int main() {
    Solution solution;
    vector<string> strs = {"flower", "flow", "flight"};
    cout << solution.longestCommonPrefix(strs) << endl;
    return 0;
}