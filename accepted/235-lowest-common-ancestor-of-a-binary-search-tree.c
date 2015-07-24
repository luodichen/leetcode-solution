/* https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) 
{
    struct TreeNode *pCur = root;
    struct TreeNode *pRet = pCur;
    
    if (p == q)
        return p;
    
    while (NULL != pCur)
    {
        pRet = pCur;
        if (pCur == p || pCur == q)
            break;
        
        struct TreeNode *pNextP = p->val < pCur->val ? pCur->left : pCur->right;
        struct TreeNode *pNextQ = q->val < pCur->val ? pCur->left : pCur->right;
        
        if (pNextP == pNextQ)
            pCur = pNextP;
        else
            break;
    }
    
    return pRet;
}
