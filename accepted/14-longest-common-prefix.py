# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if None == strs or 0 == len(strs):
            return ''
        
        ref = strs[0]
        
        for i in xrange(len(ref)):
            for j in xrange(1, len(strs)):
                if i > len(strs[j]) - 1 or strs[j][i] != ref[i]:
                    return ref[:i]
        
        return ref
