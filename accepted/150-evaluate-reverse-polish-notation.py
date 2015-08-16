# https://leetcode.com/problems/evaluate-reverse-polish-notation/
def div(x, y):
    flag = 1
    if x < 0:
        flag *= -1
        x = -x
    if y < 0:
        flag *= -1
        y = -y
    
    return x / y * flag

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if len(tokens) == 0:
            return 0
        
        symbols = set('+-*/')
        stack = []
        
        for s in tokens:
            if s in symbols:
                r = stack.pop()
                l = stack.pop()
                
                stack.append({
                              '+': lambda x, y: x + y,
                              '-': lambda x, y: x - y,
                              '*': lambda x, y: x * y,
                              '/': lambda x, y: div(x, y)}[s](l, r))
            else:
                stack.append(int(s))
        
        return stack[0]
