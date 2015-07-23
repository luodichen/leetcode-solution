# https://leetcode.com/problems/maximal-square/
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if None == matrix or len(matrix) < 1:
            return 0
        
        width = len(matrix[0])
        acc = [0] * width
        best = 0
        
        for row in matrix:
            m = {}
            for i in xrange(width):
                num = row[i]
                acc[i] = (acc[i] + 1) if num == '1' else 0
                target = acc[i]
                
                if 0 == target:
                    m = {}
                    continue
                
                max_alive = 0
                for key in m.keys():
                    if key > target:
                        if m[key] > max_alive:
                            max_alive = m[key]
                        del m[key]
                    else:
                        m[key] += 1
                    
                if not target in m:
                    m[target] = 1
                    m[target] += max_alive
                
                for (key, value) in m.items():
                    x = key if key < value else value
                    if x * x > best:
                        best = x * x
                
        return best

print Solution().maximalSquare(matrix)
