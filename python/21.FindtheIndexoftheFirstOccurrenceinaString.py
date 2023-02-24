# 暴力匹配

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            flag = True
            for j in range(n):
                if haystack[i+j] != needle[j]: # 每次匹配失败即立刻停止当前子串的匹配
                    flag = False
                    break
            if flag: # 如果完全匹配，则返回当前位置
                return i
        return -1

sol = Solution()
print(sol.strStr("butsad", "sad"))