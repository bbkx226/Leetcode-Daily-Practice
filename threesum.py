# 排序 + 双指针
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 我们枚举的三元组 (a,b,c) 满足 a≤b≤c，保证了只有 (a,b,c)这个顺序会被枚举到，而 (b,a,c)、(c,b,a)等等这些不会，这样就减少了重复

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]: 
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                
                # 如果我们固定了前两重循环枚举到的元素 a 和 b，那么只有唯一的 c 满足 a+b+c=0
                # 当第二重循环往后枚举一个元素 b′ 时，由于 b′>b，那么满足a+b′+c′=0 的c′一定有 c′<c，即 c′在数组中一定出现在 c 的左侧
                # 我们可以从小到大枚举 b，同时从大到小枚举 c，即第二重循环和第三重循环实际上是并列的关系

                # 这个方法就是我们常说的「双指针」，当我们需要枚举数组中的两个元素时，如果我们发现随着第一个元素的递增，第二个元素是递减的，
                # 那么就可以使用双指针的方法，将枚举的时间复杂度从O(N^2)减少至 O(N)

                while second < third and nums[second] + nums[third] > target: # 需要保证 b 的指针在 c 的指针的左侧
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))