from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:       
        pre = ListNode(0)
        cur = pre
        carry = 0 # Used for addition carry

        while(l1 or l2):
            x = l1.val if l1 else 0 # Check if l1 has come to the end of the Linked List
            y = l2.val if l2 else 0 # Check if l2 has come to the end of the Linked List
            sum = carry + x + y 
            carry = sum // 10 # Determine if addition carry occur
            cur.next = ListNode(sum%10)
            cur = cur.next # Only takes the tens place
            if(l1!=None):l1 = l1.next
            if(l2!=None):l2 = l2.next

        if(carry>0):
            cur.next= ListNode(1)
        li = []
        pre = pre.next
        while (pre):
            li.append(pre.val)
            pre = pre.next
        li.reverse()
        return li

sol = Solution()
nodeOne = ListNode(2)
nodeOne.next = ListNode(4)
nodeOne.next.next = ListNode(3)

nodeTwo = ListNode(5)
nodeTwo.next = ListNode(6)
nodeTwo.next.next = ListNode(4)

print(sol.addTwoNumbers(l1=nodeOne,l2=nodeTwo))