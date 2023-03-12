# 使用辅助数组
from typing import List

# matrix[row][col]，在旋转后，它的新位置为 matrixnew[col][n−row−1]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new
        return matrix

sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))