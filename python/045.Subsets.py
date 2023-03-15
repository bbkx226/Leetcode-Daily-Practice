# 迭代法实现子集枚举
# 记原序列中元素的总数为 n
# 原序列中的每个数字 ai 的状态可能有两种，即「在子集中」和「不在子集中」。我们用 1 表示「在子集中」，0 表示不在子集中，
# 那么每一个子集可以对应一个长度为 n 的 0/1 序列，第 i 位表示 ai 是否在子集中
# 可以发现 0/1 序列对应的二进制数正好从 0 到 2^n - 1
# 我们可以枚举 mask∈[0,2n−1]，mask 的二进制表示是一个 0/1 序列，
# 我们可以按照这个 0/1 序列在原集合当中取数。当我们枚举完所有 2^n个 mask，我们也就能构造出所有的子集

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, t = [], []
        for mask in range(1 << n): # bitwise left shift operator (2 raised to the power of n)
            # integer `1` is shifted to the left by `n` bits
            t.clear()
            for i in range(n):
                if (mask & (1 << i)): 
                    # Used to check whether the ith bit of mask is set to 1
                    # If the result is not 0, it means that the ith element of the input array should be included in the current subset.
                    t.append(nums[i])
            ans.append(list(t))
        return ans

sol = Solution()
print(sol.subsets([1,2,3]))