# 横向扫描
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs) # 取第一个string作为参照物
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix: # 如果self.lcp不返回任何字符串，则代表没有相符合的字串，break the for loop
                break
        # 两种情况，第一种遍历完所有字串，则返回大家都符合的prefix，第二种是大家都没有相符合的prefix，则返回“”
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0 # 寻找最短的string作为参照物， 因为prefix不可能大于它
        while index < length and str1[index] == str2[index]: # 若比较的字母的位置没超过最短string的长度，且两个字串的字母相符合，则index + 1
            index += 1
        return str1[:index]

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))