# 双指针
# 利用数组 nums1 与 nums2 已经被排序的性质
# 这一方法将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted
        return nums1

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))