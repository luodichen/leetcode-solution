# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if None == root:
            return []
        
        ret = []
        stack = [root]
        cur = root.left
        
        while None != cur or len(stack) > 0:
            if None != cur:
                stack.append(cur)
                cur = cur.left
            else:
                parent = stack.pop()
                ret.append(parent.val)
                cur = parent.right
        
        return ret
