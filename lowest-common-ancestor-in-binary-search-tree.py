class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if min(p.val, q.val) > cur.val:
                cur = cur.right
            elif max(p.val, q.val) < cur.val:
                cur = cur.left
            else:
                return cur
