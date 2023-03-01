# 动态规划
# 和第八题相似，但更简单
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*': # 如果对照串为*， 直接赋予True
                dp[0][i] = True
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j] # 若对照串为*，则比较原串或对照串的前一个字符是否相等
                    # '|' bitwise operator, which returns a value that has a 1 in any bit position where either or both of the input values have a 1
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
        return dp[m][n]

sol = Solution()
print(sol.isMatch("aa","aa*"))