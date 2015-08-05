# https://leetcode.com/problems/roman-to-integer/
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        if s is None:
            return 0
        
        roman_map = { 'I': 1, 'V': 5, 'X': 10, 'L':50, 
                     'C': 100, 'D': 500, 'M': 1000 }
        s = s.upper()
        ret = 0
        length = len(s)
        
        for i in xrange(length):
            if i < length - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                ret -= roman_map[s[i]]
            else:
                ret += roman_map[s[i]]
        
        return ret
