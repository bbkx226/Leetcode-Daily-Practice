# 使用标记数组
# 我们可以用两个标记数组分别记录每一行和每一列是否有零出现。
# 具体地，我们首先遍历该数组一次，如果某个元素为 0，那么就将该元素所在的行和列所对应标记数组的位置置为 true
# 最后我们再次遍历该数组，用标记数组更新原数组即可

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix
    
sol = Solution()
print(sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))