/* https://leetcode.com/problems/same-tree/ */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if (null == p || null == q)
        return p == q;
    else if (p.val != q.val)
        return false;
    else
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
