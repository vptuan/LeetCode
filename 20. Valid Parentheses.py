class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                return False
        return not stack
