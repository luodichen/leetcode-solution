/* https://leetcode.com/problems/minimum-size-subarray-sum/ */
int minSubArrayLen(int s, int* nums, int numsSize) 
{
    int nBegin = 0;
    int nEnd = 0;
    int nSum = 0;
    int nRet = 0;
    
    while (nEnd < numsSize)
    {
        nSum += nums[nEnd];
        int result = 0;
        while (nSum >= s)
        {
            result = nEnd - nBegin + 1;
            nSum -= nums[nBegin++];
        }
        
        if (0 == nRet || (result > 0 && result < nRet))
            nRet = result;
        
        nEnd++;
    }
    
    return nRet;
}
