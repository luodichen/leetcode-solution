# https://leetcode.com/problems/spiral-matrix-ii/
class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        ret = [[0] * n for x in xrange(n)]
        i = 1
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        
        for j in xrange(n / 2):
            for col in xrange(left, right):
                ret[top][col] = i
                i += 1
            for row in xrange(top, bottom):
                ret[row][right] = i
                i += 1
            for col in xrange(right, left, -1):
                ret[bottom][col] = i
                i += 1
            for row in xrange(bottom, top, -1):
                ret[row][left] = i
                i += 1
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        if n % 2 > 0:
            ret[n / 2][n / 2] = i
        
        return ret
