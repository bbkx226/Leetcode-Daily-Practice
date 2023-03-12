# 计算链表长度
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        cur = dummy
        length = 0
        while head:
            length += 1 # 计算出总长度
            head = head.next


        for _ in range(1, length - n + 1): #让链表遍历到需要被删除的前一个节点
            cur = cur.next

        cur.next = cur.next.next # 精髓： 让这个前节点直接连到需要被删除的节点的下一个节点
        
        li = []
        dummy = dummy.next
        while (dummy):
            li.append(dummy.val)
            dummy = dummy.next
        return li

sol = Solution()
nodeOne = ListNode(2, ListNode(4, ListNode(3, ListNode(9, ListNode(6)))))

print(sol.removeNthFromEnd(head=nodeOne, n=3))