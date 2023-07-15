# include <iostream>
# include <string>
using namespace std;

class Solution {
public:
    int strStr(string s, string p) {
        int n = s.size(), m = p.size();
        for(int i = 0; i <= n - m; i++){
            int j = i, k = 0; 
            while(k < m && s[j] == p[k]){
                j++;
                k++;
            }
            if(k == m) return i;
        }
        return -1;
    }
};

int main() {
    Solution solution;
    string s = "hello", p = "ll";
    cout << solution.strStr(s, p) << endl;
    return 0;
}