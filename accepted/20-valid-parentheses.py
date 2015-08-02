# https://leetcode.com/problems/valid-parentheses/
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        table = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        
        for c in s:
            if c in table:
                if not (len(stack) > 0 and stack.pop() == table[c]):
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
