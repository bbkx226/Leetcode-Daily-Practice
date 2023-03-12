# 双指针
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        # 由于我们需要找到倒数第 nnn 个节点，因此我们可以使用两个指针 first和 second 同时对链表进行遍历，
        # 并且 first比 second超前 n 个节点。当 first遍历到链表的末尾时，second就恰好处于倒数第 n 个节点

        for _ in range(n):
            first = first.next # 巧妙思维：首先使用 first 对链表进行遍历，遍历的次数为 n
        
        while first: 
            # 同时使用 first 和 second 对链表进行遍
            # 当 first 遍历到链表的末尾（即 first为空指针）时，second恰好指向倒数第 n 个节点。

            first = first.next
            second = second.next
        
        second.next = second.next.next

        li = []
        dummy = dummy.next
        while (dummy):
            li.append(dummy.val)
            dummy = dummy.next
        return li
    

sol = Solution()
nodeOne = ListNode(2, ListNode(4, ListNode(3, ListNode(9, ListNode(6)))))

print(sol.removeNthFromEnd(head=nodeOne, n=3))