# 单调栈
# 从左到右遍历数组，遍历到下标 i 时，如果栈内至少有两个元素，记栈顶元素为 top，top 的下面一个元素是 left，
# 则一定有 height[left]≥height[top]
# 如果 height[i]>height[top]，则得到一个可以接雨水的区域，该区域的宽度是 i−left−1，高度是 min⁡(height[left],height[i])−height[top]，
# 根据宽度和高度即可计算得到该区域能接的雨水量
# 为了得到 left，需要将 top 出栈。在对 top 计算能接的雨水量之后，left 变成新的 top，重复上述操作，直到栈变为空，或者栈顶下标对应的 height 中的元素大于或等于 height[i]

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0 # 存储最终的雨水量
        stack = list() # 存储数组 height 中的下标
        
        for i, h in enumerate(height):
            # 如果 height[i] > height[top]，则得到一个可以接雨水的区域
            while stack and h > height[stack[-1]]:
                top = stack.pop()

                # 如果 stack 中没有其他元素了，则无法计算当前位置的积水量，直接退出循环
                if not stack:
                    break
                # 否则，取出 stack 中的新的最后一个元素的下标 left，计算出当前位置 i 和左边界 left 之间的宽度
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        
        return ans

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))