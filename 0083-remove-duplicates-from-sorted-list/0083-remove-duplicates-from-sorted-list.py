# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 1 1 2
        # 1 2 3 4
        # 1 2 2 3
        
        dummy = ListNode(-200)
        dummy.next = head
        curr = dummy
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return dummy.next