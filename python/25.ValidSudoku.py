# 哈希表
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1、先生成三个数组
        rows = [[0] * 9 for _ in range(9)] # 每行
        columns = [[0] * 9 for _ in range(9)] # 每列
        box = [[[0] * 9 for _ in range(3)] for _ in range(3)] # 每个小格子
        # 遍历行
        # print(rows)
        # print(columns)
        print(box)
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    # 如果有数字则记录其位置
                    c = int(c) - 1
                    # 开始记录信息
                    rows[i][c] += 1 # 行信息
                    columns[j][c] += 1 # 列信息
                    box[i//3][j//3][c] += 1 #格信息
                    if rows[i][c] > 1 or columns[j][c]>1 or box[i//3][j//3][c]>1: # 若大于1则表示出现次数多过1，直接返回False
                        return False
        return True

sol = Solution()
board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]
print(sol.isValidSudoku(board))