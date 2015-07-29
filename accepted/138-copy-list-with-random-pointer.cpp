/* https://leetcode.com/problems/copy-list-with-random-pointer/ */
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution 
{
public:
    RandomListNode *copyRandomList(RandomListNode *head) 
    {
        if (NULL == head)
            return NULL;
        
        std::map<RandomListNode *, RandomListNode *> table;
        RandomListNode *pRet = new RandomListNode(head->label);
        RandomListNode *pSrcCur = head;
        RandomListNode *pDstCur = pRet;
        table[pSrcCur] = pDstCur;
        
        while (NULL != pSrcCur->next)
        {
            pSrcCur = pSrcCur->next;
            RandomListNode *pCopy = new RandomListNode(pSrcCur->label);
            pDstCur = pDstCur->next = pCopy;
            table[pSrcCur] = pDstCur;
        }
        
        pSrcCur = head;
        pDstCur = pRet;
        
        while (NULL != pSrcCur)
        {
            if (NULL == pSrcCur->random)
                pDstCur->random = NULL;
            else
                pDstCur->random = table[pSrcCur->random];
            
            pSrcCur = pSrcCur->next;
            pDstCur = pDstCur->next;
        }
        
        return pRet;
    }
};
