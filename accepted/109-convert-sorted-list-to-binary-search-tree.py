# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def fill_tree(self, node, head):
        if node.left is not None:
            self.fill_tree(node.left, head)
        node.val = head.val
        
        if head.next is not None:
            head.val = head.next.val
            head.next = head.next.next
            
        if node.right is not None:
            self.fill_tree(node.right, head)

    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        cur = head
        size = 0
        
        while cur is not None:
            size += 1
            cur = cur.next
        
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
        self.fill_tree(root, head)
        
        return root
