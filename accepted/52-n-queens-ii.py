# https://leetcode.com/problems/n-queens-ii/
class Solution(object):
    def check(self, n, step, row, col, left, right):
        r = step / n
        c = step % n
        
        return not row[r] and not col[c] and \
            not left[r + c] and not right[n - r + c - 1]
    
    def set(self, n, step, row, col, left, right, val):
        r = step / n
        c = step % n
        
        row[r], col[c], left[r + c], right[n - r + c - 1] = val, val, val, val
    
    def totalNQueens(self, n):
        if n < 1:
            return 0
        if n == 1:
            return 1
    
        ret = 0
        row = [False, ] * n
        col = [False, ] * n
        left = [False, ] * (2 * n - 1)
        right = [False, ] * (2 * n - 1)
        
        step = 1
        stack = [0]
        self.set(n, 0, row, col, left, right, True)
        completed = False
        
        while not completed:
            found = False
            
            while step < (len(stack) + 1) * n:
                if self.check(n, step, row, col, left, right):
                    found = True
                    break
                
                step += 1
            
            if found:
                stack.append(step)
                self.set(n, step, row, col, left, right, True)
                
            if len(stack) == n:
                solution = []
                for i in xrange(n):
                    solution.append(''.join(['Q' if j == stack[i] % n else '.' for j in xrange(n)]))
                ret += 1
            
            if len(stack) == n or not found:
                while len(stack) > 0 and stack[-1] == len(stack) * n - 1:
                    p = stack.pop()
                    self.set(n, p, row, col, left, right, False)
                
                if len(stack) == 0:
                    completed = True
                else:
                    p = stack.pop()
                    self.set(n, p, row, col, left, right, False)
                    step = p + 1
        
        return ret
