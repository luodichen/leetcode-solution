# https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def real(self, node, cur, result, root=False):
        if not root:
            cur += '->'
        cur += str(node.val)
        
        if node.left is None and node.right is None:
            result.append(cur)
            return
        
        if node.left is not None:
            self.real(node.left, cur, result)
        if node.right is not None:
            self.real(node.right, cur, result,)
        
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        
        ret = []
        self.real(root, '', ret, True)
        
        return ret
