class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for char in word:
                adj.setdefault(char, set())
        # build edges from comparisons
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if (len(w1) > len(w2) and w1[:min_len] == w2[:min_len]):
                return ""
            for j in range(min_len): # add the first different letter
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visiting = set()
        visited = set()
        res = []

        def dfs(char):
            """ create the alphabet and check for cycles """
            if char in visiting:
                return False
            elif char in visited:
                return True

            visiting.add(char) # follow the graph to the end
            for n in adj[char]:
                if not dfs(n):
                    return False
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for char in word:
                adj.setdefault(char, set())
        # build edges from comparisons
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if (len(w1) > len(w2) and w1[:min_len] == w2[:min_len]):
                return ""
            for j in range(min_len): # add the first different letter
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visiting = set()
        visited = set()
        res = deque()

        def dfs(char):
            """ create the alphabet and check for cycles """
            if char in visiting:
                return False
            elif char in visited:
                return True

            visiting.add(char) # follow the graph to the end
            for n in adj[char]:
                if not dfs(n):
                    return False
            visiting.remove(char)
            visited.add(char)

            res.appendleft(char)
            return True

        for char in adj:
            if not dfs(char):
                return ""

        return "".join(res)
