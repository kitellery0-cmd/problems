class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1c = Counter(s1)
        s2c = Counter(s2[:len(s1)])
        if s1c == s2c:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2c[s2[r]] += 1
            s2c[s2[l]] -= 1
            l += 1
            if s1c == s2c:
                return True
        return False
