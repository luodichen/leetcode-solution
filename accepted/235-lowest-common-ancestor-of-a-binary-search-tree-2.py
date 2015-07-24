# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        ret = cur
        
        if p == q:
            return p
        
        while None != cur:
            ret = cur
            if cur == p or cur == q:
                break
            
            next_p = cur.left if p.val < cur.val else cur.right
            next_q = cur.left if q.val < cur.val else cur.right
            
            if next_p == next_q:
                cur = next_p
            else:
                break
        
        return ret
