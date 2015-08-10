/* https://leetcode.com/problems/reverse-linked-list-ii/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int m, int n) 
{
    if (NULL == head || m == n)
        return head;

    struct ListNode root;
    root.next = head;
    
    struct ListNode *pLinkStart = &root;
    for (int i = 0; i < m - 1; i++)
        pLinkStart = pLinkStart->next;
    
    struct ListNode *pLinkEnd = pLinkStart->next;
    struct ListNode *pCur = pLinkEnd;
    struct ListNode *pNext = pCur->next;
    
    for (int i = 0; i < n - m; i++)
    {
        struct ListNode *pNextTmp = pNext->next;
        pNext->next = pCur;
        pCur = pNext;
        pNext = pNextTmp;
    }
    
    pLinkEnd->next = pNext;
    pLinkStart->next = pCur;
    
    return root.next;
}
