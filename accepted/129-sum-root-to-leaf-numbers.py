# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def __init__(self):
        self.stack = []
        self.result = 0
        
    def real_sum_numbers(self, node):
        self.stack.append(node.val)
        if None == node.left and None == node.right:
            sum = 0
            for num in self.stack:
                sum = sum * 10 + num
            self.result += sum
            self.stack.pop()
            return
        
        if None != node.left:
            self.real_sum_numbers(node.left)
        if None != node.right:
            self.real_sum_numbers(node.right)
        
        self.stack.pop()
        
    def sumNumbers(self, root):
        if None == root:
            return 0
        
        self.stack = []
        self.result = 0
        
        self.real_sum_numbers(root)
        return self.result

