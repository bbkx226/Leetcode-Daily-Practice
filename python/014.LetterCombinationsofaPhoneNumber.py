# 回溯
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = { # 制作哈希表表示每个数字对应的字母
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination)) # 穷举完后，把当前list加入到更大的一个总list
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter) 
                    backtrack(index + 1) # 回溯法的精髓在此
                    combination.pop() # 回溯完一个排列的所有可能性，把当前list清空，用于穷举下个排列的所有可能性

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations

sol = Solution()

print(sol.letterCombinations("234"))