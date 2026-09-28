# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(cur):
            """ returns None, p, q, or LCA """
            if not cur:
                return None
            if cur == p or cur == q:
                return cur

            left, right = dfs(cur.left), dfs(cur.right)

            if left and right: # LCA
                return cur
            return left or right 
            
        return dfs(root)
