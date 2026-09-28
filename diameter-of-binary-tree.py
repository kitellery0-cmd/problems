def diameterOfBinaryTree(root):
    def dfs(node):
        if not node:
            return (0, 0)

        left_s, right_s = dfs(node.left), dfs(node.right)
        cur_d = left_s[1] + right_s[1]
        diameter = max(left_s[0], right_s[0], cur_d)
        height = 1 + max(left_s[1], right_s[1])
        return (diameter, height)

    return dfs(root)[0]
