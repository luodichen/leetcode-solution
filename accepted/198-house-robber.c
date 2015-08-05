int rob(int* nums, int numsSize) 
{
    if (NULL == nums || 0 == numsSize)
        return 0;
    if (1 == numsSize)
        return nums[0];
    
    int nRubMax = nums[0];
    int nNotRubMax = 0;
    
    for (int i = 1; i < numsSize; i++)
    {
        int nRubTmp = nNotRubMax + nums[i];
        int nNotRubTmp = nRubMax > nNotRubMax ? nRubMax : nNotRubMax;
        nRubMax = nRubTmp;
        nNotRubMax = nNotRubTmp;
    }
    
    return nRubMax > nNotRubMax ? nRubMax : nNotRubMax;
}
