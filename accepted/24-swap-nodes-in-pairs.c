/* https://leetcode.com/problems/swap-nodes-in-pairs/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head)
{
    if (NULL == head || NULL == head->next)
        return head;

    struct ListNode *pRet = head->next;
    struct ListNode *pCur = head;
    struct ListNode *pPrev = NULL;

    while (NULL != pCur && NULL != pCur->next)
    {
        struct ListNode *pTmp = pCur->next;
        pCur->next = pCur->next->next;
        pTmp->next = pCur;
        if (NULL != pPrev)
            pPrev->next = pTmp;

        pPrev = pCur;
        pCur = pCur->next;
    }

    return pRet;
}
