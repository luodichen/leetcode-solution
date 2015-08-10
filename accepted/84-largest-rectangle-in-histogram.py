# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        best = 0
        stack = []
        for h in height:
            if len(stack) == 0 or h >= stack[len(stack) - 1][1]:
                stack.append((1, h, ))
            else:
                w = 0
                while len(stack) > 0 and stack[len(stack) - 1][1] >= h:
                    node = stack.pop()
                    w += node[0]
                    best = w * node[1] if w * node[1] > best else best
                    
                stack.append((w + 1, h, ))
        
        w = 0
        while len(stack) > 0:
            node = stack.pop()
            w += node[0]
            best = w * node[1] if w * node[1] > best else best
        
        return best
