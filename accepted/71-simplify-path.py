# https://leetcode.com/problems/simplify-path/
class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        cur = ""
        
        for i in xrange(len(path) + 1):
            c = path[i] if i < len(path) else None
            if c is None or '/' == c:
                if '.' == cur:
                    pass
                elif '..' == cur:
                    if len(stack) > 0:
                        stack.pop()
                elif len(cur) > 0:
                    stack.append(cur)
                
                cur = ""
            elif c is not None and '/' != c:
                cur += c
        
        ret = ""
        for str in stack:
            ret += "/" + str
            
        return "/" if "" == ret else ret
