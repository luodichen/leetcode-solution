# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        l = len(s)
        if l != len(t):
            return False
        
        map1 = {}
        map2 = {}
        for i in xrange(l):
            if s[i] in map1 and map1[s[i]] != t[i]:
                return False
            elif t[i] in map2 and map2[t[i]] != s[i]:
                return False
            map1[s[i]] = t[i]
            map2[t[i]] = s[i]
            
        return True
