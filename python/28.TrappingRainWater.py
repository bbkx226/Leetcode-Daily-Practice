# 动态规划
# 对于下标 i，下雨后水能到达的最大高度等于下标 i 两边的最大高度的最小值
# 下标 i 处能接的雨水量等于下标 i 处的水能到达的最大高度减去 height[i]
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        # 创建两个长度为 n 的数组 leftMax 和 rightMax
        # 对于 0≤i<n，leftMax[i] 表示下标 i 及其左边的位置中，height 的最大高度
        # rightMax[i] 表示下标 i 及其右边的位置中，height 的最大高度。

        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        # 在得到数组 leftMax 和 rightMax 的每个元素值之后，对于 0≤i<n，下标 i 处能接的雨水量等于 min⁡(leftMax[i],rightMax[i])−height[i]
        ans = 0
        for i in range(n):
            ans += min(leftMax[i], rightMax[i]) - height[i]
        return ans

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))