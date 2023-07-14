// 模拟
// Time Complexity: O(1) 
// 由于 valueSymbols 长度是固定的，且这 13 字符中的每个字符的出现次数均不会超过 3，
// 因此循环次数有一个确定的上限。对于本题给出的数据范围，循环次数不会超过 15 次。

// Space Complexity: O(1)

# include <iostream>
# include <vector>
using namespace std;

const pair<int, string> valueSymbols[] = {
    {1000, "M"},
    {900,  "CM"},
    {500,  "D"},
    {400,  "CD"},
    {100,  "C"},
    {90,   "XC"},
    {50,   "L"},
    {40,   "XL"},
    {10,   "X"},
    {9,    "IX"},
    {5,    "V"},
    {4,    "IV"},
    {1,    "I"},
};

class Solution {
public:
    string intToRoman(int num) {
        string roman;
        // const auto &[value, symbol]的auto是什么
        for (const auto &pair : valueSymbols) {
            int value = pair.first;
            const string& symbol = pair.second;
            
            while (num >= value) {
                num -= value;
                roman += symbol;
            }
            if (num == 0) {
                break;
            }
        }
        return roman;
    }
};

int main() {
    Solution s;
    int num = 1994;
    cout << s.intToRoman(num) << endl;
    return 0;
}
