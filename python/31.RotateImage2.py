# 原地旋转
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 我们应该枚举哪些位置 (row,col) 进行上述的原地交换操作呢？
        # 当 n 为偶数时，我们需要枚举 n^2 / 4 = (n/2) x (n/2) 个位置，可以将该图形分为四块
        # 当 n 为奇数时，由于中心的位置经过旋转后位置不变，我们需要枚举 (n^2−1)/4=((n−1)/2)×((n+1)/2)

        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
        return matrix
    
sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))