# https://leetcode.com/problems/anagrams/
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    
    def regular_str(self, str):
        li = list(str)
        li.sort()
        return "".join(li)
    
    def anagrams(self, strs):
        ret = []
        tb = {}
        
        for str in strs:
            regular = self.regular_str(str)
            if regular in tb:
                tb[regular] += 1
            else:
                tb[regular] = 1
        
        for str in strs:
            if tb[self.regular_str(str)] > 1:
                ret.append(str)
        
        return ret
