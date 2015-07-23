# https://leetcode.com/problems/rotate-image/
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        if 0 == len(matrix):
            return list()
        
        result = []
        col_len = len(matrix[0])
        
        for i in xrange(col_len):
            result_row = []
            for row in matrix[::-1]:
                result_row.append(row[i])
            result.append(result_row)
        
        del matrix[:]
        
        for row in result:
            matrix.append(row)
