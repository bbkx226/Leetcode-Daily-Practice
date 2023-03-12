# 哈希表
# 对于一个长度为 N 的数组，其中没有出现的最小正整数只能在 [1,N+1] 中
# 这是因为如果 [1,N] 都出现了，那么答案是 N+1 否则答案是 [1,N] 中没有出现的最小正整数
# 我们对数组进行遍历，对于遍历到的数 x，如果它在 [1,N] 的范围内
# 那么就将数组中的第 x−1 个位置（注意：数组下标从 0 开始）打上「标记」
# 在遍历结束之后，如果所有的位置都被打上了标记，那么答案是 N+1，否则答案是最小的没有打上标记的位置加 1
# 我们可以先对数组进行遍历，把不在 [1,N] 范围内的数修改成任意一个大于 N 的数（例如 N+1）
# 这样一来，数组中的所有数就都是正数了，因此我们就可以将「标记」表示为「负号」。

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0: # 我们将数组中所有小于等于 0的数修改为 N+1
                nums[i] = n + 1
        
        for i in range(n): 
            # 我们遍历数组中的每一个数 x，它可能已经被打了标记
            # 因此原本对应的数为 ∣x∣，其中 ∣ ∣为绝对值符号。如果 ∣x∣∈[1,N]，那么我们给数组中的第 ∣x∣−1 个位置的数添加一个负号
            # 注意如果它已经有负号，不需要重复添加
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
                
        # 在遍历完成之后，如果数组中的每一个数都是负数，那么答案是 N+1，否则答案是第一个正数的位置加 1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1

sol = Solution()
print(sol.firstMissingPositive([-1, 0, 1, 3]))