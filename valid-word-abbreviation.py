class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit() and abbr[j] != '0':
                start = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[ start : j ])
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False

        return (i == len(word) and j == len(abbr))
