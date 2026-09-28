class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        def find(l, r):
            num = 0
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                num += 1
                l -= 1
                r += 1
            return num
            
            
        for i in range(len(s)):
            palindromes += find(i, i) # odd
            palindromes += find(i, i + 1) # even
        return palindromes
            
