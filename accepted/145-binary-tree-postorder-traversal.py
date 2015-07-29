# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def make_node(self, node):
        ret = [node, ]
        if None != node.right:
            ret.append(node.right)
        if None != node.left:
            ret.append(node.left)
        return ret
    
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if None == root:
            return []
        
        stack = [self.make_node(root), ]
        ret = []
        
        while len(stack) > 0:
            node = stack.pop()
            if 1 == len(node):
                ret.append(node[0].val)
            else:
                next_node = self.make_node(node.pop())
                stack.append(node)
                stack.append(next_node)
        
        return ret
