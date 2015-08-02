/* https://leetcode.com/problems/insertion-sort-list/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertionSortList(struct ListNode* head)
{
    struct ListNode root;
    struct ListNode *pCur = &root;
    root.next = head;
    
    while (NULL != pCur->next)
    {
        int found = 1;
        struct ListNode *pSearch = &root;
        while (pSearch->next != pCur->next)
        {
            if (pCur->next->val <= pSearch->next->val)
            {
                struct ListNode *pNode = pCur->next;
                pCur->next = pNode->next;
                pNode->next = pSearch->next;
                pSearch->next = pNode;
                found = 0;
                break;
            }

            pSearch = pSearch->next;
        }

        if (found)
            pCur = pCur->next;
    }
    
    return root.next;
}
