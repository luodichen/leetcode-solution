/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) 
{
    struct ListNode root;
    struct ListNode *pCur = &root;
    pCur->next = head;
    
    while (NULL != pCur->next)
        if (val == pCur->next->val)
            pCur->next = pCur->next->next;
        else
            pCur = pCur->next;
    
    return root.next;
}
