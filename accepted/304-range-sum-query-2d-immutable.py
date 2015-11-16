# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix_sum = []
        
        if len(matrix) == 0:
            return
        
        row_size = len(matrix)
        col_size = len(matrix[0])
        
        for row in xrange(row_size):
            matrix_row = [0] * col_size
            for col in xrange(col_size):
                if row == 0 and col == 0:
                    matrix_row[col] = matrix[row][col]
                elif row == 0:
                    matrix_row[col] = matrix_row[col - 1] + matrix[row][col]
                elif col == 0:
                    matrix_row[col] = self.matrix_sum[row - 1][col] + matrix[row][col]
                else:
                    matrix_row[col] = matrix_row[col - 1] \
                        + self.matrix_sum[row - 1][col] \
                        + matrix[row][col] \
                        - self.matrix_sum[row - 1][col - 1]
            self.matrix_sum.append(matrix_row)

    def sumRegion(self, row1, col1, row2, col2):
        ret = self.matrix_sum[row2][col2]
        if row1 > 0:
            ret -= self.matrix_sum[row1 - 1][col2]
        if col1 > 0:
            ret -= self.matrix_sum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            ret += self.matrix_sum[row1 - 1][col1 - 1]
            
        return ret
