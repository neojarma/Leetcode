# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = None
        new = None
        nxt = head
        
        while nxt:
            org = nxt.next
            nxt.next = end
            end = nxt
            new = nxt
            nxt = org
            
        return new
            