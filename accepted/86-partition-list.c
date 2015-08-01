/* https://leetcode.com/problems/partition-list/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* partition(struct ListNode* head, int x) 
{
    struct ListNode less;
    less.next = NULL;
    struct ListNode greater;
    greater.next = NULL;
    
    struct ListNode *pLess = &less;
    struct ListNode *pGreater = &greater;
    
    struct ListNode *pCur = head;
    while (NULL != pCur)
    {
        if (pCur->val < x)
        {
            pLess->next = pCur;
            pLess = pLess->next;
        }
        else
        {
            pGreater->next = pCur;
            pGreater = pGreater->next;
        }
        
        struct ListNode *pPrev = pCur;
        pCur = pCur->next;
        pPrev->next = NULL;
    }
    
    pLess->next = greater.next;
    return less.next;
}
