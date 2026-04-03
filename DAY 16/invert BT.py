# Session 2 - Invert Binary Tree
# LeetCode #226
# Topic - Tree Traversal
# Day 13

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root:
            return None

        # swap left and right!
        root.left, root.right = root.right, root.left

        # recurse on children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Testing
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

sol = Solution()
inverted = sol.invertTree(root)

# Before:      After:
#     4            4
#    / \          / \
#   2   7        7   2
#  /\   /\      /\   /\
# 1  3 6  9    9  6 3  1