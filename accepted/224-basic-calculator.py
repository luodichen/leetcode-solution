# https://leetcode.com/problems/basic-calculator/
class Solution:
    digits = set("0123456789")
    
    def __init__(self):
        self.init()
    
    def init(self):
        self.numbers = []
        self.symbols = []
        self.num_read = False
        self.num = 0
        
    def number_got(self):
        while len(self.symbols) > 0 and self.symbols[len(self.symbols) - 1] != '(':
            right = self.numbers.pop()
            left = self.numbers.pop()
            symbol = self.symbols.pop()
            self.numbers.append(left + right if '+' == symbol else left - right)
        
    def input(self, ch):
        if ch in self.digits:
            self.num_read = True
            self.num = self.num * 10 + int(ch)
        elif ch == '+' or ch == '-' or ch == '(' or ch == ')':
            if self.num_read:
                self.numbers.append(self.num)
                self.num = 0
                self.number_got()
                
            self.num_read = False
            self.symbols.append(ch)
        
        if ch == ')':
            self.symbols.pop()
            self.symbols.pop()
            self.number_got()
        
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        self.init()
        for ch in s:
            self.input(ch)
        
        self.numbers.append(self.num)
        self.number_got()
        
        return self.numbers[0]
