# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def real_generator(self, left_left, right_left, stack, result):
        if 0 == left_left and 0 == right_left:
            result.append(''.join(stack))
            return
        if left_left > 0:
            stack.append('(')
            self.real_generator(left_left - 1, right_left, stack, result)
            stack.pop()
        if right_left > left_left:
            stack.append(')')
            self.real_generator(left_left, right_left - 1, stack, result)
            stack.pop()
            
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        stack= []
        result = []
        self.real_generator(n, n, stack, result)
        return result
