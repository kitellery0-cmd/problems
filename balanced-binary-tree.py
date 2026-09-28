class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)
            left, right = dfs(node.left), dfs(node.right)
            height = 1 + max(left[1], right[1])
            cur_balanced = abs(left[1] - right[1]) < 2
            balanced = left[0] and right[0] and cur_balanced
            return (balanced, height)

        return dfs(root)[0]


