class Solution:
    def removeCycle(self, head):
        slow = head
        fast = head

        # Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return head  # No cycle

        # Find start of cycle
        slow = head
        prev = None

        while slow != fast:
            prev = fast
            slow = slow.next
            fast = fast.next

        # Break the cycle
        prev.next = None

        return head