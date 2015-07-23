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
                acc[i] = acc[i] + 1 if num == '1' else 0
        
            result_array = [0] * width
            min_on_way = 0
            for i in xrange(width):
                min_on_way = acc[i]
                for j in xrange(i, width):
                    if acc[j] < min_on_way:
                        min_on_way = acc[j]
                    if min_on_way >= acc[i]:
                        result_array[i] += 1
                    if min_on_way >= acc[j]:
                        result_array[j] += 1
                        
            for i in xrange(width):
                if result_array[i] >= acc[i] and acc[i] * acc[i] > best:
                    best = acc[i] * acc[i]
                
        return best
