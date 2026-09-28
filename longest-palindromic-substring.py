class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r) -> tuple[int, int]:
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return (l, r)
            
        best_start = 0
        best_len = 1
        for i in range(len(s) - 1):
            for l, r in (expand(i, i), expand(i, i + 1)):
                sub_length = (r - l - 1)
                if sub_length > best_len:
                    best_len = sub_length
                    best_start = l + 1

        return s[best_start : best_start + best_len]
