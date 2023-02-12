# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == None or p == None: # 排除不是字符串的情况
            return False

        m, n = len(s), len(p)

        dp = [[False] * (n+1) for _ in range(m+1)] # 将所有项默认为 False
        
        # Special cases start here
        dp[0][0] = True # 两个空串一定匹配
        
        # s 为空串，但 p 不为空串，要想匹配，只可能是右端是星号，
        # 它干掉(* can matches zero or more of the preceding string)一个字符后，把 p 变为空串。
        for j in range(1, n+1):
            if p[j-1] == "*": dp[0][j] = dp[0][j-2] 
        # Special cases end here

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.': # 最右端的字符是匹配的，那么，大问题的答案 = 剩余子串是否匹配
                    # 从右边算起，假设只有两个字符，
                    # 只要左边的字符相等，或等于'.'(可以代表任意字符)
                    # 那么就可以让dp拿左边的字符相比较，得出结论
                    dp[i][j] = dp[i-1][j-1]
                # 右端不匹配，还不能判死刑——可能是 p[j−1]p[j-1]p[j−1] 为星号造成的不匹配，星号不是真实字符，它不匹配不算数
                # 如果 p[j−1]p[j-1]p[j−1] 不是星号，那就真的不匹配了
                elif p[j-1] == "*":
                    if s[i-1] == p[j-2] or p[j-2] == ".":
                        # p[j−1] 星号可以让 p[j−2]
                        # 在 p 串中消失(重复0次) dp[i][j-2]
                        # 出现 1 次 dp[i-1][j-2]
                        # 出现 >=2 次 dp[i-1][j]

                        # a3 情况：假设 s 的右端是一个 a，p 的右端是 a * ，* 让 a 重复 >= 2 次
                        # 星号不是真实字符，s、p是否匹配，要看 s 去掉末尾的 a，p 去掉末尾一个 a，剩下的是否匹配。
                        # 星号拷贝了 >=2 个 a，拿掉一个，剩下 >=1 个a，p 末端依旧是 a* 没变。
                        # s 末尾的 a 被抵消了，继续考察 s(0,i-2) 和 p(0,i-1) 是否匹配。
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        # s[i−1]和 p[j−2] 不匹配，还有救，p[j−1] 星号可以干掉 p[j−2]，继续考察 s(0,i−1)和 p(0,j−3)
                        dp[i][j] = dp[i][j-2]
                    print(dp)
        return dp[m][n]
        


sol = Solution()
print(sol.isMatch("s",".*"))