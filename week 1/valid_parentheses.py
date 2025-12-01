# dont like this q dont care use stack normal
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (top == '(' and ch != ')') or \
                   (top == '[' and ch != ']') or \
                   (top == '{' and ch != '}'):
                    return False       
        return not stack