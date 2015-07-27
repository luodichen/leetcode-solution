# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if None == root:
            return True
        
        lqueue = [root.left]
        rqueue = [root.right]
        
        while len(lqueue) > 0 and len(rqueue) > 0:
            l = lqueue.pop(0)
            r = rqueue.pop(0)
            
            if None != l and None != r:
                if l.val != r.val:
                    return False
            else:
                if l != r:
                    return False
            
            if None != l:
                lqueue.append(l.left)
                lqueue.append(l.right)
                rqueue.append(r.right)
                rqueue.append(r.left)
        
        return len(lqueue) == len(rqueue)
