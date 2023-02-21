# 顺序合并
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        for i in range(len(lists)):
            ans = self.mergeTwoLists(ans, lists[i])
        li = []
        ans = ans.next
        while (ans):
            li.append(ans.val)
            ans = ans.next
        return li
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: # 和MergeTwoSortedList2.py 做法一致，只是多了一个for loop, 把N个list结合在一起
        prehead = ListNode(0) # 方便进行返回
        prev = prehead # 用于遍历
        while l1 and l2: # 确保两个链表都不是None才进行比较
            if l1.val < l2.val: # 比较大小
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        prev.next = l1 if l1 is not None else l2 
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可

        return prehead.next

sol = Solution()
nodeOne = ListNode(1, ListNode(4, ListNode(5)))
nodeTwo = ListNode(1, ListNode(3, ListNode(4)))
nodeThree = ListNode(2, ListNode(6))
print(sol.mergeKLists([nodeOne, nodeTwo, nodeThree]))