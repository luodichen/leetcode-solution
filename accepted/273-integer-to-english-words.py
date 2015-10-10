# https://leetcode.com/problems/integer-to-english-words/
class Solution(object):
    def combine(self, base, left='', right=''):
        ret = base
        ret = left + ' ' + ret if ret != '' else left
        ret = ret + ' ' + right if ret != '' else right
        return ret.strip()
    
    def numberToWords(self, num):
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 
                'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty'
                ]
        
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 
                'Sixty', 'Seventy', 'Eighty', 'Ninety'
                ]
        
        hundred = 'Hundred'
        
        thousands = ['', 'Thousand', 'Million', 'Billion']
        
        ret = ''
        for i in xrange(len(thousands)):
            if 0 == num:
                break
            
            n100 = num % 1000
            numstr = ''
            if n100 >= 100:
                numstr = self.combine(numstr, right=self.combine(ones[n100 / 100], right=hundred))
            n100 %= 100
            
            if n100 > 20:
                numstr = self.combine(numstr, right=self.combine(tens[n100 / 10], right=ones[n100 % 10]))
            else:
                numstr = self.combine(numstr, right=ones[n100])
            
            num /= 1000
            
            if '' != numstr:
                ret = self.combine(thousands[i], numstr, ret)
        
        return ret if ret != '' else 'Zero'
