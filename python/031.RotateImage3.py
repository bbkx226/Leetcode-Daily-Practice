# 用翻转代替旋转
# 用翻转代替旋转 + 主对角线翻转
# KEY: matrixnew[col][n−row−1]
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
sol = Solution()

print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))