# https://leetcode.com/problems/valid-number/
class Solution:
    def __init__(self):
        self.S_FLAG = 0
        self.S_INT = 1
        self.S_DEC = 2
        self.S_INF = 3
        self.S_INX = 4
        
        self.degital = set('0123456789')
        self.flag = set('+-')
        self.dot = set('.')
        self.e = set('e')
        
        self.s_table = [self.h_flag, self.h_int, self.h_dec, self.h_iflag, self.h_index]
        
        self.accept = False
    
    def h_flag(self, c):
        if c in self.degital:
            self.accept = True
            return self.S_INT
        elif c in self.flag:
            self.accept = False
            return self.S_INT
        elif c in self.dot:
            self.accept = False
            return self.S_DEC
        else:
            return None
    
    def h_int(self, c):
        if c in self.degital:
            self.accept = True
            return self.S_INT
        elif c in self.dot:
            #self.accept = True
            return self.S_DEC
        elif c in self.e:
            if not self.accept:
                return None
            
            self.accept = False
            return self.S_INF
        else:
            return None
        
    def h_dec(self, c):
        if c in self.degital:
            self.accept = True
            return self.S_DEC
        elif c in self.e:
            if not self.accept:
                return None
            
            self.accept = False
            return self.S_INF
        else:
            return None
        
    def h_iflag(self, c):
        self.accept = c in self.degital
        return self.S_INX if c in self.degital or c in self.flag else None
    
    def h_index(self, c):
        self.accept = True
        return self.S_INX if c in self.degital else None
        
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip()
        status = self.S_FLAG
        self.accept = False
        for c in s:
            status = self.s_table[status](c)
            if status is None:
                return False
        
        return self.accept
