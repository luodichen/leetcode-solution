# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if None == root:
            return
        
        stack = [(root, 1,)]
        prev = (None , 0, )
        
        while len(stack) > 0:
            node, depth = stack.pop(0)
            if depth == prev[1]:
                prev[0].next = node
            prev = (node, depth, )
            
            if None != node.left:
                stack.append((node.left, depth + 1, ))
            if None != node.right:
                stack.append((node.right, depth + 1, ))
