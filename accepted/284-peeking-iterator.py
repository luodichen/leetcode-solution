# https://leetcode.com/problems/peeking-iterator/

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.real_next()
        
    def real_next(self):
        if self.iter.hasNext():
            self.next_num = self.iter.next()
        else:
            self.next_num = None
            
    def peek(self):
        return self.next_num

    def next(self):
        ret = self.next_num
        self.real_next()
        return ret

    def hasNext(self):
        return self.next_num is not None
