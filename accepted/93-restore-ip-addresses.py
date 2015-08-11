# https://leetcode.com/problems/restore-ip-addresses/
class Solution:
    def find_ipaddress(self, digits, stack, result):
        if len(stack) == 3 and int(digits) < 256 and not (digits[0] == '0' and len(digits) > 1):
            result.append("%s.%s.%s.%s" % (stack[0], stack[1], stack[2], digits))
        elif len(stack) < 3:
            for i in xrange(1, len(digits) - (3 - len(stack)) + 1):
                if int(digits[:i]) < 256:
                    stack.append(digits[:i])
                    self.find_ipaddress(digits[i:], stack, result)
                    stack.pop()
                else:
                    break
                
                if i == 1 and digits[0] == '0':
                    break

    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        stack = []
        result = []
        self.find_ipaddress(s, stack, result)
        
        return result
