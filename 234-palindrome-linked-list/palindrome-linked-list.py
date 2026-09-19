# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        return True