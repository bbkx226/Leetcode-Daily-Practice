# 二分查找
from typing import List

# 定理一：只有在顺序区间内才可以通过区间两端的数值判断target是否在其中
# 定理二：判断顺序区间还是乱序区间，只需要对比 left 和 right 是否是顺序对即可，left <= right，顺序区间，否则乱序区间
# 通过不断的用Mid二分，根据定理二，将整个数组划分成顺序区间和乱序区间，然后利用定理一判断target是否在顺序区间，如果在顺序区间，下次循环就直接取顺序区间，如果不在，那么下次循环就取乱序区间
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]: # 比较顺序区间在左侧或右侧
                #左侧
                if nums[0] <= target < nums[mid]: # 判断target是否在区间内
                    r = mid - 1 #若在，则直接缩小范围，不判断另一个区间
                else:
                    l = mid + 1 # 否则，判断重新判断另一个区间
            else:
                #右侧
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    
sol = Solution()
print(sol.search([1, 2, 3, 4, 5, 6, 7], 5))