# https://leetcode.com/problems/compare-version-numbers/
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        
        len1 = len(v1)
        len2 = len(v2)
        
        for i in xrange(len1 if len1 > len2 else len2):
            left = 0 if i >= len1 else v1[i]
            right = 0 if i >= len2 else v2[i]
            
            if left != right:
                return -1 if left < right else 1
            
        return 0
