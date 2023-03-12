# 变位旋转
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            res = []
            while matrix:
                # 削头（第一层）
                res += matrix.pop(0)
                # 将剩下的逆时针转九十度，等待下次被削
                matrix = list(zip(*matrix))[::-1]
                # `zip(*matrix)` is used to transpose（调换） the matrix (i.e., swap the rows and columns). This creates a new iterable object containing the transposed matrix.
            return res
    
sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))