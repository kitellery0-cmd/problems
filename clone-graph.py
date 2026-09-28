"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {} # node identity: clone

        def clone_node(node):
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(clone_node(n))
            return copy

        return clone_node(node)





# the hash map handles 1. cycles and 2. shared edges by looking up if the node
# exists yet.
