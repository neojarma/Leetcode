# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get in the middle of the ll
        # reverse the second half of the ll
        # start merging the ll with 2 ptr technique
        # l.next -> r, r.next > l.next.next, edgeg case
        # break the last connection from frist half to second half
        # link that with none
        
        # get in the middle
        # we need to get the first number in the middle
        # if the ll is even, why? because we need to break the connection
        # betwee first half and the second half
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the ll
        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # start to merge ll
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
            
        