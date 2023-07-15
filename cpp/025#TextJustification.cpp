#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string fillWords(vector<string>& words, int bg, int ed, int maxWidth, bool lastLine = false)
    {
        int wordCount = ed - bg + 1; // 单词个数
        int spaceCount = maxWidth + 1 - wordCount;  // 除去每个单词尾部空格， + 1 是最后一个单词的尾部空格的特殊处理
        for (int i = bg; i <= ed; i++)
        {
            spaceCount -= words[i].size();  // 除去所有单词的长度
        }

        int spaceSuffix = 1;    // 词尾空格
        int spaceAvg = (wordCount == 1) ? 1 : spaceCount / (wordCount - 1);     // 额外空格的平均值
        int spaceExtra = (wordCount == 1) ? 0 : spaceCount % (wordCount - 1);   // 额外空格的余数

        string ans;
        for (int i = bg; i < ed; i++)
        {
            ans += words[i];    // 填入单词
            if (lastLine)   // 特殊处理最后一行
            {
                // fill_n是C++标准库的函数，功能是在指定的区间内填充指定的值
                // back_inserter是C++标准库的迭代器，功能是在容器尾部添加元素
                fill_n(back_inserter(ans), 1, ' ');
                continue;
            }
            // 词尾空格数spaceSuffix加上平均空格数spaceAvg，如果当前索引与起始索引之差小于余数spaceExtra，则再添加一个额外的空格
            fill_n(back_inserter(ans), spaceSuffix + spaceAvg + ((i - bg) < spaceExtra), ' ');  // 根据计算结果补上空格
        }
        ans += words[ed];   // 填入最后一个单词
        fill_n(back_inserter(ans), maxWidth - ans.size(), ' '); // 补上这一行最后的空格
        return ans;
    }

    vector<string> fullJustify(vector<string>& words, int maxWidth) 
    {
        vector<string> ans;
        int cnt = 0; // 当前行的长度
        int bg = 0; // 当前行的第一个单词的下标
        for (int i = 0; i < words.size(); i++)
        {
            cnt += words[i].size() + 1; // 加上当前单词的长度和一个空格

            if (i + 1 == words.size() || cnt + words[i + 1].size() > maxWidth)
            {   // 如果是最后一个单词，或者加上下一个词就超过长度了，即可凑成一行
                ans.push_back(fillWords(words, bg, i, maxWidth, i + 1 == words.size()));
                bg = i + 1;
                cnt = 0;
            }
        }
        return ans;
    }
};

int main()
{
    Solution solution;
    vector<string> words = { "This", "is", "an", "example", "of", "text", "justification." };
    int maxWidth = 16;
    vector<string> ans = solution.fullJustify(words, maxWidth);
    for (auto& s : ans)
    {
        cout << s << endl;
    }
    return 0;
}