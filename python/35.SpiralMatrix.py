# 按层模拟

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list() # 储存需要被返回的数组
        left, right, top, bottom = 0, columns - 1, 0, rows - 1 #模拟左上和右下的方位
        while left <= right and top <= bottom:
            # 从左到右遍历上侧元素，依次为 (top,left)到 (top,right)
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            # 从上到下遍历右侧元素，依次为 (top+1,right)到 (bottom,right)
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                # 从右到左遍历下侧元素，依次为 (bottom,right−1)到 (bottom,left+1)
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                # 从下到上遍历左侧元素，依次为 (bottom,left)到 (top+1,left)
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            # 遍历完当前层的元素之后，将 left和 top 分别增加 1，将 right 和 bottom 分别减少 1，进入下一层继续遍历，直到遍历完所有元素为止
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order
sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))