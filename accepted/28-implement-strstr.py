# https://leetcode.com/problems/implement-strstr/
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        bm = {}
        needle_len = len(needle)
        for i in xrange(needle_len - 1, -1, -1):
            if needle[i] not in bm:
                bm[needle[i]] = i
        
        ret = 0
        while ret + needle_len - 1 < len(haystack):
            i = needle_len - 1
            while i >= 0:
                if haystack[ret + i] != needle[i]:
                    if haystack[ret + i] in bm and bm[haystack[ret + i]] < i:
                        ret += i - bm[haystack[ret + i]]
                    else:
                        ret += 1
                    break
                
                i -= 1
            
            if -1 == i:
                return ret
        
        return -1
