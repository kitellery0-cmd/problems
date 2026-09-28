class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        start = l = 0
        best_len = len(s) + 1
        for r in range(len(s)):
            if s[r] in need:
                if need[s[r]] > 0:
                    missing -= 1
                need[s[r]] -= 1
            if not missing:
                while s[l] not in need or need[s[l]] < 0:
                    if s[l] in need:
                        need[s[l]] += 1
                    l += 1
                cur_len = (r - l + 1)
                if cur_len < best_len:
                    best_len = cur_len
                    start = l
        if best_len == len(s) + 1:
            return ""
        return s[start : start + best_len]
