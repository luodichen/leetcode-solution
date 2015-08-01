# https://leetcode.com/problems/happy-number/
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        nums_set = set()
        while 1 != n:
            if n in nums_set:
                return False
            nums_set.add(n)
            
            new_num = 0
            while n > 0:
                new_num += (n % 10) * (n % 10)
                n /= 10
            
            n = new_num
        
        return True
