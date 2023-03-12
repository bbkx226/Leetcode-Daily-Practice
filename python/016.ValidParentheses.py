# 栈 + 哈希表
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'} 
        stack = ['?'] # 初始问号是基于若stack为空，stack.pop会报错
        for c in s:
            if c in dic: stack.append(c) # 如果括号存在于dictionary内，则添加到stack
            elif dic[stack.pop()] != c: return False # 或者如果pop掉的括号不等于相对应的符号，则直接返回false
            print(stack)
        return len(stack) == 1

sol = Solution()
print(sol.isValid('{([])}'))