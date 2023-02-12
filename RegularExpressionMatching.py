# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == None or p == None: # 排除不是字符串的情况
            return False

        m, n = len(s), len(p)

        dp = [[False] * (n+1) for _ in range(m+1)] # 将所有项默认为 False

        dp[0][0] = True # 两个空串一定匹配

        # s 为空串，但 p 不为空串，要想匹配，只可能是右端是星号，
        # 它干掉(* can matches zero or more of the preceding string)一个字符后，把 p 变为空串。
        for j in range(1, n+1):
            if p[j-1] == "*": dp[0][j] = dp[0][j-2] 

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.': 
                    # 从右边算起，假设只有两个字符，
                    # 只要左边的字符相等，或等于'.'(可以代表任意字符)
                    # 那么就可以让dp拿左边的字符相比较，得出结论
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if s[i-1] == p[j-2] or p[j-2] == ".":
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[m][n]
        


sol = Solution()
print(sol.isMatch("aaaaaa","a*"))