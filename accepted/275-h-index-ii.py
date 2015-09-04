# https://leetcode.com/problems/h-index-ii/
class Solution(object):
    def hIndex(self, citations):
        size = len(citations)
        if size < 1:
            return 0
        
        left, right = 0, size - 1
        while right - left > 1:
            mid = (left + right) / 2
            if citations[mid] >= size - mid:
                right = mid
            else:
                left = mid
                
        if citations[left] >= size - left:
            return size - left
        elif citations[right] >= size - right:
            return size - right
        else:
            return 0
