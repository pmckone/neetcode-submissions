class Solution:
    def isValid(self, s: str) -> bool:
        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []
        for p in s:
            if p in "([{":
                stack.append(p)
            if p in ")]}":
                if len(stack) == 0:
                    return False
                if stack.pop() != matching_bracket[p]:
                    return False
        if len(stack) == 0:
            return True
        return False