# 排序

# 我们用数组存储最终的答案
# 首先，我们将列表中的区间按照左端点升序排序。然后我们将第一个区间加入 数组中，并按顺序依次考虑之后的每个区间：merged
# 如果当前区间的左端点在数组 中最后一个区间的右端点之后，那么它们不会重合，我们可以直接将这个区间加入数组 的末尾；merged
# 否则，它们重合，我们需要用当前区间的右端点更新数组 中最后一个区间的右端点，将其置为二者的较大值。merged
# For Example,
# merged = [[1, 3]], 要比较的list = [2, 6]
# 由于2 < 3, b不能直接加， 需要合并
# 比较两个list中哪个的第二值比较大，就等于哪个

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sort the intervals based on their first element

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))