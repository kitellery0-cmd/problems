class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    b, a = stack.pop(), stack.pop()
                    stack.append(math.trunc(a / b))
                case _:
                    stack.append(int(token))
        return stack.pop()
