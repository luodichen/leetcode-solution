/* https://leetcode.com/problems/maximum-subarray/ */
int maxSubArray(int* nums, int numsSize)
{
    int max = nums[0];
    int cur = nums[0];

    for (int i = 1; i < numsSize; i++)
    {
        cur = (cur + nums[i]) > nums[i] ? (cur + nums[i]) : nums[i];
        if (cur > max)
            max = cur;
    }

    return max;
}
