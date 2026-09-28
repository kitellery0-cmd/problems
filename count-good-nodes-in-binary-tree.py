class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return 0
            good = 0
            if node.val >= max_val:
                max_val = node.val
                good = 1
            
            return good + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)
