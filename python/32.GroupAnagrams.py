# 排序
from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A defaultdict is a subclass of the built-in dict class that overrides one method, __missing__, 
        # to provide a default value for a nonexistent key
        # When a key is accessed that does not exist in the dictionary, 
        # instead of raising a KeyError, the __missing__ method is called and returns the default value associated with the key's data type

        # In this case, the default value associated with each key is an empty list ([])
        # So if you access a key that does not exist in the dictionary, it will automatically create a new key-value pair with the key and an empty list as the value
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st)) # 排序后加入到dict key
            mp[key].append(st) # 若没有此key，则自动创建一个key 和 它的value, which is list of values ([1, 2, 3, 4... ...])
        print(mp.values())
        return list(mp.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))