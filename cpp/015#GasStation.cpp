// 一次遍历
// Time Complexity: O(n)
// Space Complexity: O(1)

#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    // 原理：如果从i出发，到不了j(j是第一个到达不了的位置)，那么从i和j之间的任何一个位置出发都到不了j
    // 1. 首先判断总gas能不能大于等于总cost，如果总gas不够，一切都白搭对吧（总（gas - cost）不用单独去计算，和找最低点时一起计算即可，只遍历一次）；
    // 2. 再就是找总（gas-cost）的最低点，不管正负（当然如果最低点都是正的话那肯定能跑完了）；
    // 3. 找到最低点后，如果有解，那么解就是最低点的下一个点，因为总（gas-cost）是大于等于0的，所以前面损失的gas我从最低点下一个点开始都会拿回来！，别管后面的趋势是先加后减还是先减后加，最终结果我是能填平前面的坑的。
    
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int len = gas.size();
        int spare = 0;
        int minSpare = 1e9;
        int minIndex = 0;

        for (int i = 0; i < len; i++) {
            spare += gas[i] - cost[i];
            if (spare < minSpare) {
                minSpare = spare;
                minIndex = i;
            }
        }

        if(minSpare > 0) return 0;
        
        return spare < 0 ? -1 : (minIndex + 1) % len;

    }
};

int main() {
    Solution s;
    vector<int> gas = {1, 2, 3, 4, 5};
    vector<int> cost = {3, 4, 5, 1, 2};
    cout << s.canCompleteCircuit(gas, cost) << endl;
    return 0;
}