class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, -math.inf)
            
            left, right = dfs(node.left), dfs(node.right)
            left_val, right_val = max(left[0], 0), max(right[0], 0)
            
            cur_path = node.val + left_val + right_val
            best_path = max(cur_path, left[1], right[1])
            one_way = node.val + max(left_val, right_val)
            return (one_way, best_path)

        return int(dfs(root)[1])
