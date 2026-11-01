# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy  = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        sub_prev = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = sub_prev
            sub_prev = curr
            curr = next_node
        prev.next.next = curr
        prev.next = sub_prev
        return dummy.next