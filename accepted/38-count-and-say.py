# https://leetcode.com/problems/count-and-say/
class Solution:
    # @param {integer} n
    # @return {string}
    
    def countAndSay(self, n):
        if 1 == n:
            return '1'

        ret = ''
        num_str = self.countAndSay(n - 1)
        
        cur_ch = None
        count = 0
        for ch in num_str:
            if ch == cur_ch:
                count += 1
            elif None == cur_ch:
                cur_ch = ch
                count = 1
            else:
                ret += (str(count) + cur_ch)
                cur_ch = ch
                count = 1
        
        if count > 0:
            ret += (str(count) + cur_ch)
        
        return ret
