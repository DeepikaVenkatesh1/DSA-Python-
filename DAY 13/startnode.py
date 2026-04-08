class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None   # No cycle

        # Step 2: Find start node
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow