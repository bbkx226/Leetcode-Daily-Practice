# 动态规划
# 考虑最后一步可能跨了一级台阶，也可能跨了两级台阶, f(x)=f(x−1)+f(x−2)
# 我们是从第 0 级开始爬的，所以从第 0 级爬到第 0 级我们可以看作只有一种方案，即 f(0)=1
# 从第 0 级到第 1 级也只有一种方案，即爬一级，f(1)=1=
# 这两个作为边界条件就可以继续向后推导出第 n 级的正确结果。我们不妨写几项来验证一下，根据转移方程得到 f(2)=2，f(3)=3，f(4)=5，……
# 我们把这些情况都枚举出来，发现计算的结果是正确的

class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 0, 1
        for _ in range(n):
            p, q = q, r
            r = p + q
        return r

sol = Solution()
print(sol.climbStairs(5))