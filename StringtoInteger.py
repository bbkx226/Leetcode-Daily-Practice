# 自动机
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = 'start' # 起始状态
        self.sign = 1 # 表示正负号
        self.ans = 0  # 答案
        self.table = { # 状态切换表
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        
    def get_col(self, c): # 判断字符，以便于状态表内的切换并赋予状态
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c): # 核心计算
        self.state = self.table[self.state][self.get_col(c)] # 寻找状态
        if self.state == 'in_number': # 转换文字为数字， 并判断上下限
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed': # 切换正负号
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans

sol = Solution()
ans = sol.myAtoi("-123")
print(ans)
print(type(ans))