class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        length = len(s)
        
        if numRows < 2:
            return s
        
        t = 2 * (numRows - 1)
        i = 0
        ret = ""
        
        while i * t < length:
            ret += s[i * t]
            i += 1
        
        for j in xrange(1, numRows - 1):
            i = 0
            while i * t < length:
                if i * t + j < length:
                    ret += s[i * t + j]
                if (i + 1) * t - j < length:
                    ret += s[(i + 1) * t - j]
                i += 1
                                   
        
        i = 0
        while i * t + numRows - 1 < length:
            ret += s[i * t + numRows - 1]
            i += 1
        
        return ret
