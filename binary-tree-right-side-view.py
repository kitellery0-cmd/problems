class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        while q:
            rhs = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rhs = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rhs:
                res.append(rhs)
        return res
