class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            combination = []
            for string in res:
                for char in numpad[digit]:
                    combination.append(string + char)
            res = combination
        return res

# s = Solution()
# print(s.letterCombinations("34"))
