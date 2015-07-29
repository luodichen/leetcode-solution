/* https://leetcode.com/problems/same-tree/ */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public bool IsSameTree(TreeNode p, TreeNode q) {
        if (null == p || null == q)
            return p == q;
        else if (p.val != q.val)
            return false;
        else
            return IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);
    }
}
