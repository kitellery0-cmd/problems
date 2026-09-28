class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return

            left = dfs(node.left)
            if left: 
                return left
            k -= 1
            if k == 0:
                return node.val
            return dfs(node.right)

        return dfs(root)
