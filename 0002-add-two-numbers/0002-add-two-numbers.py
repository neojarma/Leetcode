# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        remain = 0
        res = ListNode(0)
        curr = res
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            total = l1val + l2val + remain

            remain = total // 10
            curr.next = ListNode(total%10)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if remain:
            curr.next = ListNode(remain)
        
        return res.next
    