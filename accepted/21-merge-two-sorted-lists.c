/* https://leetcode.com/problems/merge-two-sorted-lists/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int detect_flag(struct ListNode *pNode)
{
    if (NULL == pNode)
        return 0;
    
    int prev = pNode->val;
    pNode = pNode->next;
    
    while (NULL != pNode)
    {
        if (pNode->val > prev)
            return 1;
        else if (pNode->val < prev)
            return -1;
        pNode = pNode->next;
    }
    
    return 0;
}

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
{
    int flag = detect_flag(l1);
    if (0 == flag)
        flag = detect_flag(l2);
    if (0 == flag)
        flag = 1;
    
    struct ListNode *pRet = NULL;
    struct ListNode *pCur = pRet;
    
    while (NULL != l1 || NULL != l2)
    {
        struct ListNode *pNext = NULL;
        if (NULL == l1 || (NULL != l2 && ((l1->val - l2->val) * flag > 0)))
        {
            pNext = l2;
            l2 = l2->next;
        }
        else
        {
            pNext = l1;
            l1 = l1->next;
        }
        pNext->next = NULL;
        if (NULL == pRet)
        {
            pCur = pRet = pNext;
        }
        else
        {
            pCur->next = pNext;
            pCur = pCur->next;
        }
    }
    
    return pRet;
}
