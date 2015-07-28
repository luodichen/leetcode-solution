# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if None == root:
            return []
        
        ret = []
        cur = []
        cur_depth = 1
        
        queue = [(root, 1, )]
        
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if None != node.left:
                queue.append((node.left, depth + 1, ))
            if None != node.right:
                queue.append((node.right, depth + 1, ))
            
            if cur_depth == depth:
                cur.append(node.val)
            else:
                cur_depth = depth
                ret.append(cur)
                cur = [node.val, ]
        
        if len(cur) > 0:
            ret.append(cur)
        
        return ret
            