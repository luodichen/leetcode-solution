/* https://leetcode.com/problems/flatten-binary-tree-to-linked-list/ */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode *real_flatten(struct TreeNode *pNode)
{
    if (NULL == pNode || (NULL == pNode->left && NULL == pNode->right))
        return pNode;

    struct TreeNode *pCur = pNode;
    struct TreeNode *pRightHead = pNode->right;
    struct TreeNode *pLeft = real_flatten(pNode->left);
    struct TreeNode *pRight = real_flatten(pNode->right);

    if (NULL != pNode->left)
    {
        pNode->right = pNode->left;
        pNode->left = NULL;
        pCur = pLeft;
    }

    if (NULL != pRightHead)
    {
        pCur->right = pRightHead;
        pCur = pRight;
    }

    return pCur;
}

void flatten(struct TreeNode* root)
{
    real_flatten(root);
}
