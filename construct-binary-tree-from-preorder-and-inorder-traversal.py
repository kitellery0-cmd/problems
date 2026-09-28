class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


"""
preorder = node         -> left_subtree -> r_subtree
inorder  = left_subtree -> node         -> r_subtree

the index position of root in inorder tells us that the left subtree is:
- mid nodes after root in preorder
- the nodes to the left of root in inorder
and then we can relate this to the RHS

then we can recursively run this until the tree is constructed. by knowing this
relationship we can construct the whole tree.
"""
