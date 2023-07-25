// 在原字符串上直接判断
// Time Complexity: O(∣s∣)
// Space Complexity: O(1)
# include <iostream>
# include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        int left = 0, right = n - 1;
        while (left < right) {
            while (left < right && !isalnum(s[left])) {
                ++left;
            }
            while (left < right && !isalnum(s[right])) {
                --right;
            }
            
            if (left < right) {
                if (tolower(s[left]) != tolower(s[right])) {
                    return false;
                }
                ++left;
                --right;
            }
        }
        return true;
    }
};

int main(){
    Solution s;
    cout << s.isPalindrome("A man, a plan, a canal: Panama");
}
