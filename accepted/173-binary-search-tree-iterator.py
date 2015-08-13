# https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.find_smallest(root)
        
    def find_smallest(self, node):
        cur = node
        while cur is not None:
            self.stack.append(cur)
            cur = cur.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return 0 != len(self.stack)

    # @return an integer, the next smallest number
    def next(self):
        if not self.hasNext():
            return None
        
        node = self.stack.pop()
        self.find_smallest(node.right)
        
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())