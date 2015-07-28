/* https://leetcode.com/problems/linked-list-cycle-ii/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head)
{
    if (NULL == head || NULL == head->next)
        return NULL;

    struct ListNode *pSlow = head->next;
    struct ListNode *pFast = head->next->next;

    while (NULL != pFast && NULL != pFast->next && pFast != pSlow)
    {
        pSlow = pSlow->next;
        pFast = pFast->next->next;
    }

    if (NULL == pFast || NULL == pFast->next)
        return NULL;

    pSlow = head;
    while (pSlow != pFast)
    {
        pSlow = pSlow->next;
        pFast = pFast->next;
    }

    return pSlow;
}
