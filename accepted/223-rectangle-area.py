# https://leetcode.com/problems/rectangle-area/
class Solution:
    def cross(self, a, b, c, d):
        l = [a, b, c, d, ]
        l.sort()
        s = set([l[0][1], ])
        
        ret = 0
        for i in xrange(1, len(l)):
            if 2 == len(s):
                ret += l[i][0] - l[i - 1][0]
            if l[i][1] in s:
                s.remove(l[i][1])
            else:
                s.add(l[i][1])
        
        return ret
    
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        x_cross = self.cross((A, 0, ), (C, 0, ), (E, 1, ), (G, 1, ))
        y_cross = self.cross((B, 0, ), (D, 0, ), (F, 1, ), (H, 1, ))
        
        cross = x_cross * y_cross
        return (C - A) * (D - B) + (G - E) * (H - F) - cross
