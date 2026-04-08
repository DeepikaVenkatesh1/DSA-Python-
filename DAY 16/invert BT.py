class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root:
            return None

        # swap left and right
        root.left, root.right = root.right, root.left

        # recurse on children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root