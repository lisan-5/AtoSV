from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "*/+-":
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(b + a)
                elif token == "*":
                    stack.append(b * a)
                elif token == "/":
                    # Division that truncates towards zero
                    stack.append(int(b / a))
                elif token == "-":
                    stack.append(b - a)

        return stack[0]
