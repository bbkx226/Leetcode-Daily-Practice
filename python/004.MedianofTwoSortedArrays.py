# 二分查找
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k): # k 为 (m+n)/2 或 (m+n)/2 + 1
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1, 那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2, 那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                # 如果一个数组为空，说明该数组中的所有元素都被排除，我们可以直接返回另一个数组中第k小的元素。
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                # 如果 k=1，我们只要返回两个数组首元素的最小值即可
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                # 两个数组的下标
                newIndex1 = min(index1 + k // 2 - 1, m - 1) #用min来避免position大于list长度
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                # 找出下标相对应的数字
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                #1 如果 A[k/2 − 1] < B[k/2 − 1]，则比 A[k/2 − 1]小的数最多只有 A的前 k/2 − 1个数和 B的前 k/2 − 1个数，
                # 即比 A[k/2 − 1] 小的数最多只有 k−2 个，因此 A[k/2 − 1]不可能是第 k个数，A[0]到 A[k/2 − 1]也都不可能是第 k数，可以全部排除。
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1 # 根据我们排除数的个数，减少 k 的值，这是因为我们排除的数都不大于第 k 小的数
                    index1 = newIndex1 + 1 # 假装排除了小于的个数，实则将position挪后
                #2 如果 A[k/2−1]>B[k/2−1]，则可以排除 B[0]到 B[k/2−1].
                #3 如果 A[k/2−1]=B[k/2−1]，则可以归入第一种情况处理。
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

sol = Solution()
print(sol.findMedianSortedArrays(nums1=[1, 2, 3, 4], nums2=[5, 6, 7]))