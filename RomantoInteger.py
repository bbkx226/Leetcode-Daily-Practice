# 模拟
class Solution:
    def __init__(self):
        self.symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            val = self.symbol[c] # 找出对应integer
            if i < len(s) - 1 and val < self.symbol[s[i+1]]: 
            # 如果position不是最后一个，且后一位character代表的数值大于当前字符，则需要拿它减去当前的值
                ans -= val
            else:
                ans += val
        return ans
    
sol = Solution()
print(sol.romanToInt("XIV"))
        
