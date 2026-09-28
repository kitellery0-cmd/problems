class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def add_word(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.word = word
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)
        rows = len(board)
        cols = len(board[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def in_bounds(r, c):
            return True if (0 <= r < rows and 0 <= c < cols) else False
        
        res = []
        visiting = set()
        def search(r, c, cur):
            if len(res) == len(words):
                return
            if (not in_bounds(r, c) or
                (r, c) in visiting or
                board[r][c] not in cur.children):
                return
            
            cur = cur.children[board[r][c]]
            if cur.word:
                res.append(cur.word)
                cur.word = False
            visiting.add((r, c))
            for rc, cc in dirs:
                search(r + rc, c + cc, cur)
            visiting.remove((r, c))
            return

        for r in range(rows):
            for c in range(cols):
                search(r, c, root)
                if len(res) == len(words):
                    return words

        return res

