# https://leetcode.com/problems/game-of-life/
class Solution(object):
    def gameOfLife(self, board):
        if board is None or len(board) == 0:
            return
        
        height = len(board)
        width = len(board[0])
        prev_row = [0] * (width + 2)
        prev = 0
        
        for j in xrange(height):
            cur = list(board[j])
            prev = 0
            for i in xrange(1, width + 1):
                neighbor = prev_row[i - 1] + prev_row[i] + prev_row[i + 1] + prev
                if i < width:
                    neighbor += board[j][i]
                if j < height - 1:
                    neighbor += board[j + 1][i - 1]
                    if i > 1:
                        neighbor += board[j + 1][i - 2]
                    if i < width:
                        neighbor += board[j + 1][i]
                
                prev = board[j][i - 1]
                
                if neighbor < 2 or neighbor > 3:
                    board[j][i - 1] = 0
                elif neighbor == 3:
                    board[j][i - 1] = 1
            
            prev_row[1:-1] = cur
