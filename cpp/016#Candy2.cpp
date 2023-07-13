// 常数空间遍历
// Time Complexity: O(n)
// Space Complexity: O(1)

# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        int ret = 1; // 第一个孩子的糖果数量为 1
        int inc = 1, dec = 0, pre = 1; // inc: 递增序列的长度, dec: 递减序列的长度, pre: 前一个同学分得的糖果数量
        for (int i = 1; i < n; i++) {
            // 如果当前同学比上一个同学评分高，说明我们就在最近的递增序列中，直接分配给该同学 pre+1 个糖果即可
            if (ratings[i] >= ratings[i - 1]) {
                // 递减序列的长度清零
                dec = 0;
                // 如果当前同学的分数大于前一个同学，则直接分配给该同学 pre + 1 个糖果
                pre = ratings[i] == ratings[i - 1] ? 1 : pre + 1;
                // 累加当前同学分得的糖果数量
                ret += pre;
                inc = pre;
            } else { // 否则我们就在一个递减序列中，我们直接分配给当前同学一个糖果，并把该同学所在的递减序列中所有的同学都再多分配一个糖果，以保证糖果数量还是满足条件
            // 我们无需显式地额外分配糖果，只需要记录当前的递减序列长度，即可知道需要额外分配的糖果数量
            // 同时注意当当前的递减序列长度和上一个递增序列等长时，需要把最近的递增序列的最后一个同学也并进递减序列中
            // 这样，我们只要记录当前递减序列的长度 dec，最近的递增序列的长度 inc 和前一个同学分得的糖果数量 pre 即可
                dec++;

                if (dec == inc) {
                    dec++;
                }
                ret += dec;
                pre = 1;
            }
        }
        return ret;
    }
};

int main() {
    Solution s;
    vector<int> ratings = {1, 3, 5, 3, 2, 1};
    cout << s.candy(ratings) << endl;
    return 0;
}