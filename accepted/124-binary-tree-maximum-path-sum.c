/* https://leetcode.com/problems/binary-tree-maximum-path-sum/ */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int real_max_path(struct TreeNode *pNode, int *result)
{
    if (NULL == pNode)
        return 0;
    
    int nLeftSum = real_max_path(pNode->left, result);
    int nRightSum = real_max_path(pNode->right, result);
    
    int nMax = nLeftSum > nRightSum ? nLeftSum : nRightSum;
    int nRet = pNode->val + (nMax > 0 ? nMax : 0);
    
    int nSum = pNode->val;
    if (nLeftSum > 0) nSum += nLeftSum;
    if (nRightSum > 0) nSum += nRightSum;
    if (nSum > *result) *result = nSum;
    
    return nRet;
}

int maxPathSum(struct TreeNode* root) 
{
    if (NULL == root)
        return 0;
    
    int result = root->val;
    real_max_path(root, &result);
    
    return result;
}
