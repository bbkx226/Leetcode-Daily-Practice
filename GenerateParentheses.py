# 回溯法
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            print(left, right) # 跟踪到目前为止放置的左括号和右括号的数目
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n: # 如果左括号数量不大于 n，我们可以放一个左括号
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
                print(S, "Hi")
            if right < left: # 如果右括号数量小于左括号的数量，我们可以放一个右括号
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()
                print(S, "Test")

        backtrack([], 0, 0) 
        return ans

sol = Solution()
print(sol.generateParenthesis(2))