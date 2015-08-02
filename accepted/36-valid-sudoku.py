# https://leetcode.com/problems/valid-sudoku/
class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if 9 != len(board) or 9 != len(board[0]):
            return False
        
        row_set = None
        cell_sets = None
        
        for row in xrange(9):
            row_set = set()
            if 0 == row % 3:
                cell_sets = [set() for i in xrange(3)]
            for col in xrange(9):
                ch = board[row][col]
                if ch == '.':
                    continue
                if ord(ch) < ord('0') or ord(ch) > ord('9'):
                    return False
                if ch in row_set:
                    return False
                row_set.add(ch)
                if ch in cell_sets[col / 3]:
                    return False
                cell_sets[col / 3].add(ch)
        
        col_set = None
        for col in xrange(9):
            col_set = set()
            for row in xrange(9):
                ch = board[row][col]
                if ch == '.':
                    continue
                if ch in col_set:
                    return False
                col_set.add(ch)
        
        return True
