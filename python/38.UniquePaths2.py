# 组合数学
import math
# 从左上角到右下角的过程中，我们需要移动 m+n−2次，其中有 m−1次向下移动，n−1 次向右移动
# 因此路径的总数，就等于从 m+n−2 次移动中选择 m−1 次向下移动的方案数
# 即组合数：(m+n-2)! / (m-1)!(n-1)!
# 因此我们直接计算出这个组合数即可。计算的方法有很多种：
# 如果使用的语言有组合数计算的 API，我们可以调用 API 计算；
# 如果没有相应的 API，我们可以使用 (m+n−2)(m+n−3)⋯ n / (m−1)! 进行计算

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # math.comb(n, k): Find the total number of possibilities to choose k things from n items
        return math.comb(m + n - 2, n - 1) # or math.comb(m + n - 2, m - 1)

sol = Solution()
print(sol.uniquePaths(3, 7))