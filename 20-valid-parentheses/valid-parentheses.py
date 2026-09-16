class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        top = -1

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
                top += 1

            if ch == ')':
                if not stack:
                    return False
                elif stack[top] == '(':
                    stack.pop()
                    top -= 1
                else:
                    return False
            elif ch == '}':
                if not stack:
                    return False
                elif stack[top] == '{':
                    stack.pop()
                    top -= 1
                else:
                    return False
            elif ch == ']':
                if not stack:
                    return False
                elif stack[top] == '[':
                    stack.pop()
                    top -= 1
                else:
                    return False
        if not stack:
            return True
        else:
            return False