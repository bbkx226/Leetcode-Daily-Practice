from typing import List

class Solution:
    # List[int] is a type hint in Python that specifies that the function argument nums is a list of integers
    # The examples omitted examples of how to annotate the type of a function’s return value ('-> List[int]')
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hashtable = dict() # Create a hashtable
        # `enumerate()` allows you to loop over a list (or other iterable) and get both the index and the value of each element
        for i, num in enumerate(nums):
            if target - num in hashtable: 
                return [hashtable[target - num], i]
            # If nothing matched, push the key (number) & value (position) into the hashtable
            hashtable[nums[i]] = i
        return []

sol = Solution()
print(sol.twoSum(nums=[3, 5, 3, 9], target=6))