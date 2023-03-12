# 使用一个标记变量

# 我们可以对方法二进一步优化，只使用一个标记变量记录第一列是否原本存在 0
# 这样，第一列的第一个元素即可以标记第一行是否出现 0
# 为了防止每一列的第一个元素被提前更新，我们需要从最后一行开始，倒序地处理矩阵元素
# 比如下面这个矩阵:
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]

# 按照算法三, 我们之所以要从后面开始处理, 是因为如果我们先处理了第一行那么矩阵变成了
#  [0,0,0,0],
#  [3,4,5,2],
#  [1,3,1,5]

# 第一行的第二列和第三列的0元素影响了下面的 4, 5 和3, 1
# 但是其实这两个0不是本来存在的, 而是处理之后出现的
# 所以我们从下面处理, 就不会被这两个0影响了

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    
        #  为了防止每一列的第一个元素被提前更新，我们需要从最后一行开始，倒序地处理矩阵元素
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0 
        return matrix
    
sol = Solution()
print(sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
