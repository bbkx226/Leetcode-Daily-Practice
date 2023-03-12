# 使用两个标记变量

# 我们可以用矩阵的第一行和第一列代替方法一中的两个标记数组，以达到 O(1)的额外空间
# 但这样会导致原数组的第一行和第一列被修改，无法记录它们是否原本包含 0
# 因此我们需要额外使用两个标记变量分别记录第一行和第一列是否原本包含 0
# 在实际代码中，我们首先预处理出两个标记变量，接着使用其他行与列去处理第一行与第一列，
# 然后反过来使用第一行与第一列去更新其他行与列，最后使用两个标记变量更新第一行与第一列即可
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))
        
        # 我们首先预处理出两个标记变量，接着使用其他行与列去处理第一行与第一列，
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # 然后反过来使用第一行与第一列去更新其他行与列，最后使用两个标记变量更新第一行与第一列即可
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0
        return matrix
    
sol = Solution()
print(sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))