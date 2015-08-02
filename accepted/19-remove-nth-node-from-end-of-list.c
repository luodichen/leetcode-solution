/* https://leetcode.com/problems/remove-nth-node-from-end-of-list/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode root;
    root.next = head;
    struct ListNode *pFast = &root;
    struct ListNode *pSlow = &root;

    while (n--)
        pFast = pFast->next;

    while (NULL != pFast->next)
    {
        pFast = pFast->next;
        pSlow = pSlow->next;
    }

    pSlow->next = pSlow->next->next;

    return root.next;
}
