# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.stack = []
        self.result_p = None
        self.result_q = None
    
    def search(self, node, p, q):
        self.stack.append(node)
        
        if node is p:
            self.result_p = list(self.stack)
        if node is q:
            self.result_q = list(self.stack)
        
        if node.left is not None:
            self.search(node.left, p, q)
        if node.right is not None:
            self.search(node.right, p, q)
        
        self.stack.pop()

    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if None == root:
            return None
        
        i = 0
        ret = None
        self.search(root, p, q)
        
        while i < len(self.result_p) and i < len(self.result_q):
            if self.result_p[i] is self.result_q[i]:
                ret = self.result_p[i]
            i += 1
        
        return ret
