# 动态规划
# 用 f(i)代表以第 i个数结尾的「连续子数组的最大和」
# 我们只需要求出每个位置的 f(i)，然后返回 f 数组中的最大值即可

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, maxAns = 0, nums[0]
        for i in nums:
            pre = max(pre + i, i) #遍历每个数，找出i position中最大的值
            maxAns = max(maxAns, pre)# 再通过取max，来得到数组中最大的值
        return maxAns
    
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))