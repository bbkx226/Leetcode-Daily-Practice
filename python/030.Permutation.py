# 回溯
class Solution:
    def permute(self, nums):
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:]) #  appends a copy of the list nums to another list res.
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作, 意即让转换后的数组变为标准，例如from [0, 2, 1] to [0, 1, 2]
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res
    
sol = Solution()
print(sol.permute([0, 1, 2, 3, 4]))