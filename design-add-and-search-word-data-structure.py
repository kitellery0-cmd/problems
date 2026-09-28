class TrieNode:
    def __init__(self):
        self.children = {}      # char -> node
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(idx, cur):
            if idx == len(word):
                return cur.end
            elif word[idx] in cur.children:
                return dfs(idx + 1, cur.children[word[idx]])
            elif word[idx] == '.':
                for child_node in cur.children.values():
                    if dfs(idx + 1, child_node):
                        return True
                return False
            else:
                return False

        return dfs(0, self.root)
