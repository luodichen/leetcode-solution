/* https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/ */
int removeDuplicates(int* nums, int numsSize) 
{
    if (NULL == nums || numsSize < 2)
        return numsSize;
    
    int nCur = *nums;
    int nCount = 1;
    int *pWrite = nums + 1;
    
    for (int i = 1; i < numsSize; i++)
    {
        if (nCur != nums[i])
            nCount = 0;
        
        if (nCount < 2)
        {
            nCount++;
            *pWrite++ = nums[i];
            nCur = nums[i];
        }
    }
    
    return pWrite - nums;
}
