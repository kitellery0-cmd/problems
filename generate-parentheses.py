class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(openp, closedp, string):
            if openp == closedp == n:
                res.append(string)
                return
            if openp < n:
                generate(openp + 1, closedp, string + '(')
            if closedp < openp:
                generate(openp, closedp + 1, string + ')')

        generate(0, 0, "")
        return res
