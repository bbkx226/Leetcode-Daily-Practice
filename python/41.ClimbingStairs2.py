# 斐波那契数列
# 公式： Fn = (1 / sqrt. 5) * ((1 + sqrt.5) / 2)^n - ((1- sqrt.5) / 2)^n
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt_5 = 5 ** 0.5
        fib_n = ((1 + sqrt_5) / 2) ** (n + 1) - ((1 - sqrt_5) / 2) ** (n + 1)
        return int(fib_n / sqrt_5)


sol = Solution()
print(sol.climbStairs(5))