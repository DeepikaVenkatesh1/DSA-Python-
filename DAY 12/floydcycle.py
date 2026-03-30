# Define ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps

            if slow == fast:          # cycle detected
                return True

        return False                  # no cycle


# Testing
# Case 1: No cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

sol = Solution()
print(sol.hasCycle(head))   # Output: False


# Case 2: Create a cycle manually
head.next.next.next = head.next   # 3 -> 2 (cycle)

print(sol.hasCycle(head))   # Output: True