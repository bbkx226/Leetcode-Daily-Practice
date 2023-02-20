# 递归
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: # 若 l1 为空， 直接返回 l2
            return l2
        elif l2 is None: # 若 l2 为空， 直接返回 l1
            return l1
        elif l1.val < l2.val: # 比较值， 若一开始 l1 < l2，则l1.next，直接merge，进行下一轮的比较
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else: # 繁殖， 则以l2 为基准开始merge
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

sol = Solution()
nodeOne = ListNode(2, ListNode(4, ListNode(3, ListNode(9, ListNode(6)))))
nodeTwo = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(sol.mergeTwoLists(nodeOne, nodeTwo))
