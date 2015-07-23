# https://leetcode.com/problems/plus-one/
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        cur = len(digits) - 1
        digits[cur] += 1
        
        while cur > 0:
            if digits[cur] > 9:
                digits[cur - 1] += 1
                digits[cur] %= 10
                cur -= 1
            else:
                break
        
        if 0 == cur and digits[0] > 9:
            digits[0] = 1
            digits.append(0)
        
        return digits
