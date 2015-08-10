# https://leetcode.com/problems/merge-k-sorted-lists/
class PriorityQueue(object):
    def __init__(self, order):
        self.heap = []
        self.order = order
    
    def swim(self, index):
        while (index - 1) / 2 >= 0:
            parent = (index - 1) / 2
            if (self.heap[parent].val - self.heap[index].val) * self.order > 0:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break
    
    def sink(self, index):
        while index * 2 + 1 < len(self.heap):
            child = index * 2 + 1
            child += 0 if child + 1 == len(self.heap) or \
                (self.heap[child + 1].val - self.heap[child].val) * self.order > 0 else 1
            
            if (self.heap[index].val - self.heap[child].val) * self.order > 0:
                self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                index = child
            else:
                break
    
    def size(self):
        return len(self.heap)
    
    def first(self):
        return self.heap[0]
    
    def pop_first(self):
        ret = self.first()
        
        if self.size() > 1:
            self.heap[0] = self.heap.pop()
            self.sink(0)
        else:
            self.heap.pop()
        
        return ret
    
    def insert(self, node):
        self.heap.append(node)
        self.swim(len(self.heap) - 1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        order = 0
        for head in lists:
            cur = head
            while cur is not None and cur.next is not None and order != 0:
                if cur.val < cur.next.val:
                    order = 1
                    break
                elif cur.val > cur.next.val:
                    order = -1
                    break
                else:
                    cur = cur.next
            if order != 0:
                break
        
        if 0 == order:
            order = 1
        
        pq = PriorityQueue(order)
        for head in lists:
            if head is not None:
                pq.insert(head)
        
        ret_head = ListNode(0)
        ret_head.next = None
        
        cur = ret_head
        while pq.size() > 0:
            cur.next = pq.pop_first()
            cur = cur.next
            
            if cur.next is not None:
                pq.insert(cur.next)
                cur.next = None
        
        return ret_head.next
