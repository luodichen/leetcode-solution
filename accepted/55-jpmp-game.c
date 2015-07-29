/* https://leetcode.com/problems/jump-game/ */
bool canJump(int* nums, int numsSize) 
{
    int nFarthest = 0;
    for (int i = 0; (i < numsSize && i <= nFarthest); i++)
    {
        if (i + nums[i] > nFarthest)
            nFarthest = i + nums[i];
    }
    
    return nFarthest >= numsSize - 1;
}
