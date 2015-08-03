# https://leetcode.com/problems/fraction-to-recurring-decimal/
class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        flag = 1
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            flag = -1
        
        numerator = -numerator if numerator < 0 else numerator
        denominator = -denominator if denominator < 0 else denominator
        
        integer_part = numerator / denominator
        
        decimal_stack = []
        remainder_stack = []
        remainder_set = set()
        
        recurring = None
        
        numerator %= denominator
        
        while numerator > 0:
            if numerator not in remainder_set:
                remainder_set.add(numerator)
                remainder_stack.append(numerator)
                decimal_stack.append(((numerator * 10) / denominator))
                numerator = (numerator * 10) % denominator
            else:
                recurring = []
                prev = None
                while prev != numerator:
                    recurring.insert(0, decimal_stack.pop())
                    prev = remainder_stack.pop()
                break
        
        ret = "" if 1 == flag else "-"
        ret += str(integer_part)
        
        if len(decimal_stack) > 0 or recurring is not None:
            ret += "."
        
        for i in decimal_stack:
            ret += str(i)
        
        if recurring is not None:
            ret += '('
            for i in recurring:
                ret += str(i)
            ret += ')'
        
        return ret
