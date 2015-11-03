/* https://leetcode.com/problems/longest-increasing-subsequence/ */

int lengthOfLIS(int* nums, int numsSize) 
{
    if (0 == numsSize)
        return 0;
    
    int nRet = 1;
    int *dp = (int *)malloc(numsSize * sizeof(int));
    dp[0] = 1;
    
    for (int i = 1; i < numsSize; i++)
    {
        int nResult = 1;
        for (int j = 0; j < i; j++)
            if (dp[j] >= nResult && nums[i] > nums[j])
                nResult = dp[j] + 1;
        
        dp[i] = nResult;
        nRet = nResult > nRet ? nResult : nRet;
    }
    free((void *)dp);
    
    return nRet;
}
