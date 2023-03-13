# 单指针

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        # 在第一次遍历中，我们从左向右遍历整个数组，如果找到了 0，那么就需要将 0 与「头部」位置的元素进行交换，并将「头部」向后扩充一个位置
        # 在遍历结束之后，所有的 0 都被交换到「头部」的范围，并且「头部」只包含 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

        # 在第二次遍历中，我们从「头部」开始，从左向右遍历整个数组，如果找到了 1，那么就需要将 1 与「头部」位置的元素进行交换，并将「头部」向后扩充一个位置
        # 在遍历结束之后，所有的 1 都被交换到「头部」的范围，并且都在 0 之后，此时 2 只出现在「头部」之外的位置，因此排序完成
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        return nums

sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))