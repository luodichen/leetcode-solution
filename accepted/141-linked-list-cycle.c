/* https://leetcode.com/problems/linked-list-cycle/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *pFast = head;
    struct ListNode *pSlow = head;
    
    while (NULL != pFast && NULL != pFast->next)
    {
        pSlow = pSlow->next;
        pFast = pFast->next->next;
        
        if (pSlow == pFast)
            return true;
    }
    
    return false;
}
