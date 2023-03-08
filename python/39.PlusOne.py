# 巧妙解法

# 根据题意加一，没错就是加一这很重要，因为它是只加一的所以有可能的情况就只有两种：
# 除 9 之外的数字加一
# 数字 9

# 加一得十进一位个位数为 0 加法运算如不出现进位就运算结束了且进位只会是一
# 所以只需要判断有没有进位并模拟出它的进位方式，如十位数加 1 个位数置为 0，如此循环直到判断没有再进位就退出循环返回结果
# 然后还有一些特殊情况就是当出现 99、999 之类的数字时，循环到最后也需要进位，出现这种情况时需要手动将它进一位

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10 # 判断有没有进位
            if digits[i] != 0: # 如果不是0，即digits[i] ！= 10
                return digits
        # 特殊情况，手动进位
        digits = [0] * (n + 1)
        digits[0] = 1
        return digits
sol = Solution()
print(10%10)
print(sol.plusOne([4,3,2,1]))