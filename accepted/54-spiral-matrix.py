# https://leetcode.com/problems/spiral-matrix/
class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if None == matrix or 0 == len(matrix):
            return list()
        
        width = len(matrix[0])
        height = len(matrix)
        
        leftX = 0
        rightX = width - 1
        
        topY = 0
        bottomY = height - 1
        
        ret = []
        count = 0
        
        while leftX <= rightX and topY <= bottomY:
            for i in xrange(leftX, rightX):
                if count < width * height:
                    ret.append(matrix[topY][i])
                count += 1
            for i in xrange(topY, bottomY):
                if count < width * height:
                    ret.append(matrix[i][rightX])
                count += 1
            for i in xrange(rightX, leftX, -1):
                if count < width * height:
                    ret.append(matrix[bottomY][i])
                count += 1
            for i in xrange(bottomY, topY, -1):
                if count < width * height:
                    ret.append(matrix[i][leftX])
                count += 1
            
            leftX += 1
            rightX -= 1
            topY += 1
            bottomY -= 1
            
        if width == height and width % 2 != 0 and count < width * height:
            ret.append(matrix[(width - 1) / 2][(width - 1) / 2])
            count += 1
        
        return ret
