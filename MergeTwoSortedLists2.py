# 迭代
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1) # 方便进行返回

        prev = prehead # 用于遍历
        while l1 and l2: # 确保两个链表都不是None才进行比较
            if l1.val <= l2.val: # 比较大小
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        prev.next = l1 if l1 is not None else l2 
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可

        return prehead.next