class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        bools = [False] * (len(s) + 1)
        bools[-1] = True
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                pos = i + len(word)
                if (pos <= len(s) and
                    bools[pos] and
                    s[i : pos] == word):
                    bools[i] = True
                    break
                    
        return bools[0]
