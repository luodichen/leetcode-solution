# https://leetcode.com/problems/merge-intervals/
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        ret = []
        handler_list = []
        for element in intervals:
            handler_list.append((element.start, 1, ))
            handler_list.append((element.end, -1, ))
            
        handler_list.sort(cmp=lambda x, y: x[0] - y[0] if (x[0] != y[0]) else y[1] - x[1])
        
        count = 0
        start = None
        #for element in handler_list:
        for i in xrange(len(handler_list)):
            element = handler_list[i]
            count += element[1]
            if 1 == count and start is None:
                start = element[0]
            elif 0 == count and (len(handler_list) - 1 == i or (handler_list[i + 1][0] != element[0])):
                ret.append([start, element[0], ])
                start = None
        
        return ret
