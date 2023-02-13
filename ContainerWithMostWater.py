from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
            l, r = 0, len(height) - 1
            ans = 0
            while l < r:
                area = min(height[l], height[r]) * (r - l)
                ans = max(ans, area)
                # 考虑第一步，假设当前左指针和右指针指向的数分别为 x 和 y，不失一般性，我们假设 x≤y
                # 同时，两个指针之间的距离为 tt。那么，它们组成的容器的容量为：
                # min⁡(x,y)∗t=x∗t
                # 我们可以断定，如果我们保持左指针的位置不变，那么无论右指针在哪里，这个容器的容量都不会超过 x∗t了。
                # 注意这里右指针只能向左移动，因为 我们考虑的是第一步，也就是 指针还指向数组的左右边界的时候。
                # 我们任意向左移动右指针，指向的数为 y1，两个指针之间的距离为 t1
                # 那么显然有 t1<t
                # 并且 min⁡(x,y1)≤min⁡(x,y):
                # 如果 y1≤y 那么 min⁡(x,y1)≤min⁡(x,y)
                # 如果 y1>y，那么 min⁡(x,y1)=x=min⁡(x,y)
                # 因此有：min(x,yt)∗t1 < min(x,y)∗t
                # 即无论我们怎么移动右指针，得到的容器的容量都小于移动前容器的容量。
                # 也就是说，这个左指针对应的数不会作为容器的边界了，那么我们就可以丢弃这个位置，
                # 将左指针向右移动一个位置，此时新的左指针于原先的右指针之间的左右位置，才可能会作为容器的边
                if height[l] <= height[r]:
                    l += 1
                else:
                    r -= 1
            return ans

sol = Solution()
print(sol.maxArea([1, 4, 5, 6, 7, 8, 3, 9, 5]))