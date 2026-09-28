class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif self.isSame(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or
                    self.isSubtree(root.right, subRoot))


    def isSame(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif (not root or not subRoot) or (root.val != subRoot.val):
            return False
        return (self.isSame(root.left, subRoot.left) and
                self.isSame(root.right, subRoot.right))
