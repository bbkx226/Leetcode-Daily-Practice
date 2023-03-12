# 二分查找
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftIdx = self.binarySearch(nums, target, True) # 数组中「第一个等于 target 的位置」
        rightIdx = self.binarySearch(nums, target, False) - 1 # 「第一个大于 target 的位置减一」
        if leftIdx <= rightIdx and rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target:
            return [leftIdx, rightIdx]
        return [-1, -1]

    def binarySearch(self, nums: List[int], target: int, lower: bool) -> int:
        left, right, ans = 0, len(nums) - 1, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans

sol = Solution()
print(sol.searchRange([1,2,2,3,3,4,5,6,7], 2))