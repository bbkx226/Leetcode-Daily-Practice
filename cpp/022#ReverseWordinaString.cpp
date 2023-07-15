# include <iostream>
# include <string>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        s = ' ' + s; // 特殊情况转为统一处理
        int n = s.size();
        string ans;
        for (int left = n - 1, right = n; left >=0; left--) {
            if (s[left] == ' ') { // 特殊情况转为统一处理
                if (left + 1 < right) { // 防止连续空格的情况
                    ans += s.substr(left + 1, right - left - 1); // 为什么是right - left - 1? 因为substr的第二个参数是长度
                    ans += ' ';
                }
                right = left; // 让right紧跟left，避免连续多个空格被甩开，导致添加单词时候里面有多余空格
            }
        }
        return ans.substr(0, ans.size() - 1); //结尾处理一下多余空格
        
    }
};

int main() {
    Solution solution;
    string s = "the sky is blue";
    cout << solution.reverseWords(s) << endl;
    return 0;
}