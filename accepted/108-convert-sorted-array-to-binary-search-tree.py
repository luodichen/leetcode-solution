# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def fill_tree(self, node, nums):
        if node.right is not None:
            self.fill_tree(node.right, nums)
        node.val = nums.pop()
        if node.left is not None:
            self.fill_tree(node.left, nums)

    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        size = len(nums)
        if 0 == size:
            return None
        
        root = TreeNode(0)
        queue = [root, ]
        
        i = 1
        while i < size:
            parent = queue.pop(0)
            parent.left = TreeNode(0)
            queue.append(parent.left)
            i += 1
            
            if i == size:
                break
            
            parent.right = TreeNode(0)
            queue.append(parent.right)
            i += 1
        
        queue = None
        self.fill_tree(root, nums)
        
        return root
