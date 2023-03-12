# 快速幂 + 递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0: # 0次方直接返回 1
                return 1.0
            y = quickMul(N // 2) # 不断递归
            return y * y if N % 2 == 0 else y * y * x #若次方为奇数，则进行特别处理
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n) # 数学逻辑，若幂小于0，则答案为倒数

sol = Solution()
print(sol.myPow(2, 6))