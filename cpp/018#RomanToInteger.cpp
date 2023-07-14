# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    // 按照题目的描述，可以总结如下规则：
    // 罗马数字由 I,V,X,L,C,D,M 构成；
    // 当小值在大值的左边，则减小值，如 IV=5-1=4；
    // 当小值在大值的右边，则加小值，如 VI=5+1=6；
    // 由上可知，右值永远为正，因此最后一位必然为正。
    // 一言蔽之，把一个小值放在大值的左边，就是做减法，否则为加法。
    int romanToInt(string s) {
        int sum = 0;
        int preNum = getValue(s[0]);
        
        for (int i = 1; i < s.length(); i++) {
            int num = getValue(s[i]);
            
            if (preNum < num) {
                sum -= preNum;
            } else {
                sum += preNum;
            }
            
            preNum = num;
        }
        
        // 在代码实现上，可以往后看多一位，对比当前位与后一位的大小关系，从而确定当前位是加还是减法。当没有下一位时，做加法即可。
        sum += preNum;
        return sum;
    }
    
private:
    int getValue(char ch) {
        switch (ch) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
};

int main() {
    Solution s;
    string str = "MCMXCIV";
    cout << s.romanToInt(str) << endl;
    return 0;
}