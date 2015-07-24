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
    def getPath(self, root, node):
        cur = root
        ret = []
        while cur.val != node.val:
            ret.append(cur)
            cur = cur.left if node.val < cur.val else cur.right
        ret.append(cur)
        return ret
    
    def lowestCommonAncestor(self, root, p, q):
        if None == root:
            return None
        p_path = self.getPath(root, p)
        q_path = self.getPath(root, q)
        
        ret = root
        i = 1
        
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            ret = p_path[i]
            i += 1
        
        return ret
