# 中心扩展算法

class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]: # 如果两边的字母不同，我们就可以停止扩展
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)): # i 决定字串从哪个位置开始扩张
            l1, r1 = self.expandAroundCenter(s, i, i) # 子串长度为 1
            l2, r2 = self.expandAroundCenter(s, i, i + 1) # 子串长度为 2
            if r1 - l1 > end - start: # 比 max length 大小
                start, end = l1, r1
            if r2 - l2 > end - start: # 比 max length 大小
                start, end = l2, r2

        return s[start: end + 1]

sol = Solution()
print(sol.longestPalindrome("abba"))