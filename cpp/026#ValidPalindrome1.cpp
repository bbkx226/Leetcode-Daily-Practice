// 双指针
// Time Complexity: O(∣s∣)
// Space Complexity: O(∣s∣)
# include <iostream>
# include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string sgood;
        // 将字符串中的字母和数字字符保留在另一个字符串中
        for (char ch: s) {
            // isalnum() 函数用来判断指定的字符是否为字母或数字，是则返回非零值，否则返回 0
            if (isalnum(ch)) {
                sgood += tolower(ch); // tolower() 函数用来把大写字符转换为小写字符
            }
        }
        int n = sgood.size();
        int left = 0, right = n - 1;
        // 双指针
        while (left < right) {
           if (sgood[left] != sgood[right]) {
                return false;
            }
            ++left;
            --right;
        }
        return true;
    }
};

int main(){
    Solution s;
    cout << s.isPalindrome("A man, a plan, a canal: Panama");
}
