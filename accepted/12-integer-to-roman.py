# https://leetcode.com/problems/integer-to-roman/
class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        table = [['', 'M', 'MM', 'MMM', 'MMMM'],
                 ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                 ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                 ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]
        ret = ''
        n = 10 ** (len(table) - 1)
        for i in xrange(len(table)):
            ret += table[i][num / n]
            num %= n
            n /= 10
        return ret
