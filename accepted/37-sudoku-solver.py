# https://leetcode.com/problems/sudoku-solver/
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
        
    def init(self, board):
        self.row_set = [set() for _ in xrange(9)]
        self.col_set = [set() for _ in xrange(9)]
        self.sell_set = [set() for _ in xrange(9)]
        self.fill = []
        
        for row in xrange(9):
            for col in xrange(9):
                if '.' != board[row][col]:
                    num = board[row][col]
                    self.row_set[row].add(num)
                    self.col_set[col].add(num)
                    self.sell_set[row / 3 * 3 + col / 3].add(num)
                else:
                    board[row][col] = '0'
                    self.fill.append((row, col, ))
        
    def solveSudoku(self, board):
        self.init(board)
        i = 0

        while i < len(self.fill):
            row, col = self.fill[i]
            found = False
            num = board[row][col]
            if num != '0':
                self.row_set[row].remove(num)
                self.col_set[col].remove(num)
                self.sell_set[row / 3 * 3 + col / 3].remove(num)
                
            for k in xrange(int(num) + 1, 10):
                k = str(k)
                if k not in self.row_set[row] \
                        and k not in self.col_set[col] \
                        and k not in self.sell_set[row / 3 * 3 + col / 3]:
                    found = True
                    self.row_set[row].add(k)
                    self.col_set[col].add(k)
                    self.sell_set[row / 3 * 3 + col / 3].add(k)
                    board[row][col] = k
                    
                    break
            
            if found:
                i += 1
            else:
                board[row][col] = '0'
                i -= 1
            
            if i < 0:
                return
    