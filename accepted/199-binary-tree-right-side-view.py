# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if None == root:
            return []
        
        cur_level = 0
        ret = []
        queue = [(root, 1), ]
        
        while len(queue) > 0:
            node, level = queue.pop(0)
            if cur_level != level:
                ret.append(node.val)
                cur_level = level
            
            if None != node.right:
                queue.append((node.right, level + 1, ))
            if None != node.left:
                queue.append((node.left, level + 1, ))
        
        return ret
