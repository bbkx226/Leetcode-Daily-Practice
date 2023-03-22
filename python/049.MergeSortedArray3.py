# 逆向双指针

# 方法二中，之所以要使用临时变量，是因为如果直接合并到数组 nums1 中，nums1 中的元素可能会在取出之前被覆盖
# 那么如何直接避免覆盖 nums1 中的元素呢？观察可知，nums1 的后半部分是空的，可以直接覆盖而不会影响结果
# 因此可以指针设置为从后向前遍历，每次取两者之中的较大者放进 nums1 的最后面
# 严格来说，在此遍历过程中的任意一个时刻，nums1数组中有 m−p1−1 个元素被放入 nums1 的后半部，
# nums2 数组中有 n−p2−1个元素被放入 nums1 的后半部，而在指针 p1 的后面，nums1 数组有 m+n−p1−1 个位置

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
        return nums1

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))