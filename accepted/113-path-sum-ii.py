# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    
    def real_path_sum(self, node, sum, stack, result, cur_sum):
        stack.append(node.val)
        cur_sum += node.val
        
        if None == node.left and None == node.right:
            if cur_sum == sum:
                result.append(list(stack))
            stack.pop()
            return
        
        if None != node.left:
            self.real_path_sum(node.left, sum, stack, result, cur_sum)
        if None != node.right:
            self.real_path_sum(node.right, sum, stack, result, cur_sum)
            
        stack.pop()
    
    def pathSum(self, root, sum):
        if None == root:
            return []
        
        stack = []
        result = []
        
        self.real_path_sum(root, sum, stack, result, 0)
        return result