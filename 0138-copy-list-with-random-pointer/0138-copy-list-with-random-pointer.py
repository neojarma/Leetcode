"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # map => {[node]: newnode} => newnode.next = [old.next]
        if not head:
            return head
        old = {}
        cpy = head
        while cpy:
            old[cpy] = Node(cpy.val)
            cpy = cpy.next

        cpy = head
        while cpy:
            newNode = old[cpy]
            newNode.next = old.get(cpy.next)
            newNode.random = old.get(cpy.random)
            cpy = cpy.next

        return old[head]