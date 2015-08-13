# https://leetcode.com/problems/basic-calculator-ii/
class Solution:
    digits = set('0123456789')
    symbolset = set('+-*/()')
    
    def __init__(self):
        self.init()
    
    def init(self):
        self.numbers = []
        self.symbols = []
        self.num_read = False
        self.num = 0
        
    def number_got(self, priority):
        while len(self.symbols) > 0 and self.symbols[len(self.symbols) - 1] != '(':
            if priority > 0 and self.symbols[len(self.symbols) - 1] in set('+-'):
                break
            
            right = self.numbers.pop()
            left = self.numbers.pop()
            symbol = self.symbols.pop()
            
            result = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
                      '*': lambda a, b: a * b, '/': lambda a, b: a / b,
                     }[symbol](left, right)

            self.numbers.append(result)
        
    def input(self, ch):
        if ch in self.digits:
            self.num_read = True
            self.num = self.num * 10 + int(ch)
        elif ch in self.symbolset:
            if self.num_read:
                self.numbers.append(self.num)
                self.num = 0
                self.number_got({'(': 0, ')': 0, '+': 0, '-': 0, '*': 1, '/': 1, }[ch])
                
            self.num_read = False
            self.symbols.append(ch)
        
        if ch == ')':
            self.symbols.pop()
            self.symbols.pop()
            self.number_got(0)
        
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        self.init()
        for ch in s:
            self.input(ch)
        
        self.numbers.append(self.num)
        self.number_got(0)
        
        return self.numbers[0]

print Solution().calculate('1+4')