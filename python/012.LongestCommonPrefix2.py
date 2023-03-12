from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                # any 返回 boolean
                # 当第一个子串的length达到第二个比较的子串的length，或者子串中的字母不相符时，则直接返回相符的子串
                return strs[0][:i]
        
        return strs[0]