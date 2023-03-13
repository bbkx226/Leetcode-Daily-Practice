# 双指针
# 如果找到了 1，那么将其与 nums[p1] 进行交换，并将 p1 向后移动一个位置，这与方法一是相同的
# 如果找到了 0，那么将其与 nums[p0] 进行交换，并将 p0 向后移动一个位置。这样做是正确的吗？我们可以注意到，因为连续的 0 之后是连续的 1
# 因此如果我们将 0 与 nums[p0] 进行交换，那么我们可能会把一个 1 交换出去
# 当 p0 < p1时，我们已经将一些 1 连续地放在头部，此时一定会把一个 1 交换出去，导致答案错误
# 因此，如果 p0 < p1，那么我们需要再将 nums[i] 与 nums[p1]进行交换，其中 i 是当前遍历到的位置，在进行了第一次交换后，nums[i] 的值为 1
# 我们需要将这个 1 放到「头部」的末端
# 在最后，无论是否有 p0 < p1，我们需要将 p0 和 p1 均向后移动一个位置，而不是仅将 p0 向后移动一个位置
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
        return nums
sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))