class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next

        for _ in range(right - left):
            next_node = cur.next

            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next