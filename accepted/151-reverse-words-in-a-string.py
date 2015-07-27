# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        cur = ""
        ret = ""
        result = []
        for c in s:
            if ' ' == c and len(cur) > 0:
                result.append(cur)
                cur = ""
            elif ' ' != c:
                cur += c
        if len(cur) > 0:
            result.append(cur)
        
        reverse = result[::-1]
        for i in xrange(len(reverse)):
            ret += (" " + reverse[i]) if i > 0 else reverse[i]
        
        return ret
