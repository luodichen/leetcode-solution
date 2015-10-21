# https://leetcode.com/problems/find-median-from-data-stream/

class Heap(object):
    def __init__(self, compare=None):
        self.mHeap = list()
        self.mCompare = (lambda x, y: x - y) if compare is None else compare
    
    def put(self, n):
        self.mHeap.append(n)
        cur = len(self.mHeap) - 1
        
        parent = (cur - 1) / 2
        while cur > 0 and self.mCompare(self.mHeap[parent], self.mHeap[cur]) > 0:
            self.mHeap[parent], self.mHeap[cur] = self.mHeap[cur], self.mHeap[parent]
            cur = parent
            parent = (cur - 1) / 2
    
    def get(self):
        if len(self.mHeap) == 0:
            return None
        elif len(self.mHeap) == 1:
            return self.mHeap.pop()
        
        ret = self.mHeap[0]
        self.mHeap[0] = self.mHeap.pop()
        
        cur = 0
        
        while cur * 2 + 1 < len(self.mHeap):
            if cur * 2 + 2 == len(self.mHeap):
                next = cur * 2 + 1
            else:
                next = (cur * 2 + 1) if self.mCompare(self.mHeap[cur * 2 + 1], 
                            self.mHeap[cur * 2 + 2]) < 0 else (cur * 2 + 2)
            
            if self.mCompare(self.mHeap[cur], self.mHeap[next]) > 0:
                self.mHeap[cur], self.mHeap[next] = self.mHeap[next], self.mHeap[cur]
                cur = next
            else:
                break
        
        return ret
            
    def empty(self):
        return len(self.mHeap) == 0

class MedianFinder:
    def __init__(self):
        self.mLeftHeap = Heap(lambda x, y: y - x)
        self.mRightHeap = Heap(lambda x, y: x - y)
        self.mMiddle = []

    def addNum(self, num):
        if len(self.mMiddle) == 0:
            self.mMiddle.append(num)
        elif len(self.mMiddle) == 1:
            target = self.mLeftHeap if num < self.mMiddle[0] else self.mRightHeap
            if target is not None:
                target.put(num)
                num = target.get()
            
            self.mMiddle.append(num)
            if self.mMiddle[0] > self.mMiddle[1]:
                self.mMiddle[0], self.mMiddle[1] = self.mMiddle[1], self.mMiddle[0]
        else:
            if num < self.mMiddle[0]:
                self.mLeftHeap.put(num)
                self.mRightHeap.put(self.mMiddle.pop())
            elif num < self.mMiddle[1]:
                self.mRightHeap.put(self.mMiddle.pop())
                self.mLeftHeap.put(self.mMiddle.pop())
                self.mMiddle.append(num)
            else:
                self.mRightHeap.put(num)
                self.mLeftHeap.put(self.mMiddle[0])
                self.mMiddle = [self.mMiddle[1], ]
        
    def findMedian(self):
        if len(self.mMiddle) == 0:
            return None
        elif len(self.mMiddle) == 1:
            return self.mMiddle[0] * 1.0
        else:
            return sum(self.mMiddle) / 2.0
