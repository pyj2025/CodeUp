class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        num = 0
        sign = "+"

        for idx, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and not ch.isspace()) or (idx == (len(s) - 1)):
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    prev = stack.pop()
                    stack.append(num * prev)
                elif sign == "/":
                    prev = stack.pop()
                    
                    if prev // num < 0 and prev % num != 0:
                        stack.append(prev // num + 1)
                    else:
                        stack.append(prev // num)

                sign = ch
                num = 0

        return sum(stack)
    
                