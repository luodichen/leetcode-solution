# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        ret = 0
        flag = 1
        wating_flag = True
        
        for c in str.strip():
            if '-' == c and wating_flag:
                flag = -flag
                wating_flag = False
            elif '+' == c and wating_flag:
                wating_flag = False
            elif ord(c) < ord('0') or ord(c) > ord('9'):
                return ret * flag
            else:
                ret = ret * 10 + ord(c) - ord('0')
                if 1 == flag and ret > INT_MAX:
                    ret = INT_MAX
                elif -1 == flag and -ret < INT_MIN:
                    ret = -INT_MIN
                wating_flag = False
        
        return ret * flag
