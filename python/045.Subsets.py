# 迭代法实现子集枚举
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
                    t.append(nums[i])
            ans.append(list(t))
        return ans

sol = Solution()
print(sol.subsets([1,2,3]))