/* https://leetcode.com/problems/add-two-numbers/ */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{
    struct ListNode root;
    struct ListNode *pCur = &root;
    int flag = 0;
    root.next = NULL;
    
    while (NULL != l1 || NULL != l2)
    {
        struct ListNode *pNewNode = (struct ListNode *)malloc(sizeof(struct ListNode));
        pNewNode->next = NULL;
        
        int v1 = NULL == l1 ? 0 : l1->val;
        int v2 = NULL == l2 ? 0 : l2->val;
        
        pNewNode->val = (v1 + v2 + flag) % 10;
        flag = (v1 + v2 + flag) / 10;
        
        pCur = pCur->next = pNewNode;
        
        l1 = (NULL == l1) ? NULL : l1->next;
        l2 = (NULL == l2) ? NULL : l2->next;
    }
    
    if (flag > 0)
    {
        struct ListNode *pNewNode = (struct ListNode *)malloc(sizeof(struct ListNode));
        pNewNode->next = NULL;
        pNewNode->val = flag;
        
        pCur = pCur->next = pNewNode;
    }
    
    return root.next;
}
