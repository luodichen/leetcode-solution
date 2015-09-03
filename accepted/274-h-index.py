# https://leetcode.com/problems/h-index/
class Solution(object):
    def hIndex(self, citations):
        citations.sort(cmp=lambda a, b: b - a)

        ret = 0
        for i in xrange(len(citations)):
            if not citations[i] > i:
                break
            ret += 1
        
        return ret
