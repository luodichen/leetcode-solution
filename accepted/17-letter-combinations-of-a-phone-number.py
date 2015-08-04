# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def __init__(self):
        self.digit_map = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', 
                          '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', 
                          '9': 'wxyz'}
    
    def real_lc(self, digits, stack, result):
        if 0 == len(digits):
            result.append(''.join(stack))
            return
        
        for s in self.digit_map[digits[0]]:
            stack.append(s)
            self.real_lc(digits[1:], stack, result)
            stack.pop()
        
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if digits is None or 0 == len(digits):
            return []
        
        result = []
        stack = []
        self.real_lc(digits, stack, result)
        
        return result
