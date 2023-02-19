# 栈

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        stack = []

        while cur:
            stack.append(cur) # 将所有链表加入到list中
            cur = cur.next 
        
        for _ in range(n): stack.pop() # 通过题目给予的n，把list最后一个element依次删除

        pre = stack[-1] # 这是通过了stack栈的特性，这样pre就能顺理成章地继承链表被删除节点的前一个结点
        pre.next = pre.next.next # 此时再让这个前节点直接连到需要被删除的节点的下一个节点

        li = []
        dummy = dummy.next
        while (dummy):
            li.append(dummy.val)
            dummy = dummy.next
        return li

sol = Solution()
nodeOne = ListNode(2, ListNode(4, ListNode(3, ListNode(9, ListNode(6)))))

print(sol.removeNthFromEnd(head=nodeOne, n=3))