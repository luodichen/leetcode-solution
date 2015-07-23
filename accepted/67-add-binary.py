# https://leetcode.com/problems/add-binary/
class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        lena = len(a)
        lenb = len(b)
        flag = '0'
        ret = ""
        for i in xrange(lena if lena > lenb else lenb):
            ca = a[lena - i - 1] if i < lena else '0'
            cb = b[lenb - i - 1] if i < lenb else '0'
            
            cur = '0' if ca == cb else '1'
            n_flag = '1' if '1' == ca and '1' == cb else '0'
            n_flag = '1' if '1' == cur and '1' == flag else n_flag
            cur = '0' if cur == flag else '1'
            
            flag = n_flag
            ret += cur
        
        if '1' == flag:
            ret += '1'
        
        return ret[::-1]
