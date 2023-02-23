# 双指针
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        # fast 用于表示遍历数组到达的下标位置， slow表示下一个不同元素要填入的下标位置
        fast = slow = 1 # 从第二个pos开始，因为第一个pos的号码永远不重复
        while fast < n:
            if nums[fast] != nums[fast - 1]: # 检测是否与上一个数字相同
                nums[slow] = nums[fast] # 如果不是，则替换slow指针的数字
                slow += 1
            fast += 1
        
        return slow # 返回长度

sol = Solution()
print(sol.removeDuplicates([1, 1, 1, 2, 2, 3, 4, 5, 5]))