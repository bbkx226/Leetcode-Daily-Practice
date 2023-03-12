# 双指针
# 由于数组 leftMax 是从左往右计算，数组 rightMax 是从右往左计算
# 因此可以使用双指针和两个变量代替两个数组
# 维护两个指针 left 和 right，以及两个变量 leftMax 和 rightMax
# 初始时 left=0,right=n−1,leftMax=0,rightMax=0
# 指针 left 只会向右移动，指针 right 只会向左移动
# 在移动指针的过程中维护两个变量 leftMax 和 rightMax 的值
# 当两个指针没有相遇时，进行如下操作：
# 使用 height[left] 和 height[right]的值更新 leftMax和 rightMax 的值
# 如果 height[left] < height[right]，则必有 leftMax<rightMax, 下标 left 处能接的雨水量等于 leftMax−height[left]，将下标 left 处能接的雨水量加到能接的雨水总量，然后将 left 加 1（即向右移动一位）
# 如果 height[left] ≥ height[right]，则必有 leftMax ≥ rightMax，下标 right 处能接的雨水量等于 rightMax−height[right]，将下标 right 处能接的雨水量加到能接的雨水总量，然后将 right 减 1（即向左移动一位）
# 当两个指针相遇时，即可得到能接的雨水总量

# ”必有“ 的解释:
# if (height[left] < height[right]) {
#     left++;
# } else {
#     right--;
# }
# 如果当前轮的双指针为 left 和 right，那么上一轮要么是 left - 1 和 right，要么是 left 和 right + 1
# 如果移动的是 left 指针，即 left - 1 -> left，那么 height[0, left- 1] < height[right] 且 height[right] = rightMax
# 如果移动的是 right 指针，即 right <- right + 1，那么 height[left] >= height[right + 1, n - 1] 且 height[left] = leftMax
# 现在，我们再回看官方的描述： 如果 height[left] < height[right]，则必有 leftMax < rightMax
# 假设上一轮移动的是 left 指针，有 height[0, left- 1] < height[right]，又 height[left] < height[right]，则 height[0, left] < height[right] = rightMax
# 假设上一轮移动的是 right 指针，有 height[left] >= height[right + 1, n - 1]，又 height[left] < height[right]，则 leftMax = height[left] < height[right]

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        
        return ans

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
