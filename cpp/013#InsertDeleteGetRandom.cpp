// 变长数组 + 哈希表
// Time Complexity: O(1)
// Space Complexity: O(n)

#include <iostream>
#include <unordered_map>
#include <random>
using namespace std;

class RandomizedSet {
    public:
        unordered_map<int,int> m;
        vector<int> v;

        RandomizedSet() {
            
        }
        
        bool insert(int val) {
            // 如果val不在哈希表中，那么将val插入到数组的末尾，同时在哈希表中记录val的下标
            // 为什么要插入到数组末尾? 因为数组是变长数组，插入到数组末尾的时间复杂度是O(1)
            // 何为变长数组？就是数组的大小可以动态改变，不像C语言中的数组大小是固定的
            if(m.count(val)==0){
                m[val]=v.size();
                // push_back()函数将val插入到数组的末尾
                v.push_back(val);
                return true;
            }
            return false;
        }
        
        bool remove(int val) {
            if(m.count(val)){
                // 如果val在哈希表中，那么将val对应的下标与数组末尾的元素交换，同时更新哈希表
                int tt=v[v.size()-1]; // tt = 数组末尾的元素
                m[tt]=m[val];

                // 将需要被删除的元素放到最后，然后pop_back()删除
                swap(tt,v[m[val]]);
                v.pop_back();

                // 删除哈希表中val的记录
                m.erase(val);
                return true;
            }
            return false;
        }
        
        int getRandom() {
            // rand()函数返回一个随机数, rand() % n 返回一个0到n-1的随机数
            int idx = (rand() % (v.size()));
            return v[idx];
        }
};

int main() {
    RandomizedSet* obj = new RandomizedSet();
    bool param_1 = obj->insert(1);
    bool param_2 = obj->remove(2);
    int param_3 = obj->getRandom();
    cout << param_1 << param_2 << param_3;
    return 0;
}
