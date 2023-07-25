// 双指针
// Time Complexity: O(m+n)
// Space Complexity: O(1)
# include <iostream>
# include <string>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n = s.length(), m = t.length();
        int i = 0, j = 0;
        //
        while (i < n && j < m) {
            if (s[i] == t[j]) {
                i++;
            }
            j++;
        }
        return i == n;
    }
};

int main(){
    Solution s;
    cout << s.isSubsequence("abc", "ahbgdc");
}