/* https://leetcode.com/problems/insertion-sort-list/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* insertionSortList(struct ListNode* head)
{
    struct ListNode root;
    struct ListNode *pCur = head;
    struct ListNode *pPrev = &root;
    root.next = head;
    
    while (NULL != pCur)
    {
        struct ListNode *pSearch = &root;
        struct ListNode *pNext = pCur->next;
        while (pSearch->next != pCur)
        {
            if (pSearch->next->val >= pCur->val)
            {
                pPrev->next = pCur->next;
                pCur->next = pSearch->next;
                pSearch->next = pCur;
                break;
            }
            
            pSearch = pSearch->next;
        }
        
        pPrev = pCur;
        pCur = pNext;
    }
    
    return root.next;
}
