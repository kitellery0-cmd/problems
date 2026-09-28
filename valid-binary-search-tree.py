class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(lower, node, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return (valid(lower, node.left, node.val) and 
                    valid(node.val, node.right, upper))

        return valid(float("-inf"), root, float("inf"))
