# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        stack = []
        water = 0
        for h in height:
            tmp = 0
            w = 1
            bottom = 0
            width_total = 0
            
            while len(stack) > 0 and stack[len(stack) - 1][1] < h:
                width, bottom = stack.pop()
                tmp += bottom * width
                width_total += width
                w += width

            wall = bottom if len(stack) == 0 else stack[len(stack) - 1]
                
            water += (h if h < wall else wall) * width_total - tmp
            stack.append((w, h, ))
            
        return water
