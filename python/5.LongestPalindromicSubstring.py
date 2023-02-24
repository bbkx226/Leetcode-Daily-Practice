# 动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: # 小于2,自己就是自己的回文，可以直接返回原字符串
            return s
        
        max_len = 1 # 不可能为0， 因为即使只有1个字母，其也会是自己的回文，因此最小为1
        begin = 0 # 用于返回字串是，字符串中的位置
        
        dp = [[False] * n for _ in range(n)] # dp[i][j] 表示 s[i..j] 是否是回文串

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1): # 只考虑大于2的字串，因此 2 ... n+1, L即此时此刻需要比较的字串长度(2, 3, 4....)
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]: # 不相同时直接返回 False
                    dp[i][j] = False 
                else:
                    if j - i < 3: # 当字串长度小于3，即 1 或 2时， 由于字母相同，可以直接赋予True
                        dp[i][j] = True
                    else: # 如果大于3， 则需要往内比较，例： abba中，如果s[0]和s[3]相同，则需要往内，取s[1]及s[2]进行比较，若为True，则这个字串的回文便被认可
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1 # 取代原本最长子串的长度
                    begin = i # 更改起始位置
                print(dp)

        return s[begin:begin + max_len]

sol = Solution()
print(sol.longestPalindrome("adcbbcda"))