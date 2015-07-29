/* https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head)
{
    if (NULL == head)
        return NULL;

    struct ListNode root;
    struct ListNode *pLast = &root;
    root.next = NULL;

    struct ListNode *pPrev = head;
    struct ListNode *pCur = head->next;

    int dup = 0;
    while (NULL != pCur)
    {
        if (pCur->val == pPrev->val)
        {
            dup = 1;
        }
        else if (dup != 0)
        {
            dup = 0;
        }
        else
        {
            pLast->next = pPrev;
            pLast = pLast->next;
            pLast->next = NULL;
        }

        pPrev = pCur;
        pCur = pCur->next;
    }

    if (0 == dup)
    {
        pLast->next = pPrev;
        pLast->next->next = NULL;
    }

    return root.next;
}
