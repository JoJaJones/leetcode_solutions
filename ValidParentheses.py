class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matches = {
            '(':')',
            '{': '}',
            '[': ']'
        }
        for char in s:
            if char in matches:
                stack.append(char)
            elif char in ')}]':
                if len(stack) == 0:
                    return False
                
                if matches[stack[-1]] != char:
                    return False
                
                stack.pop()
        
        return len(stack) == 0
