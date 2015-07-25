/* https://leetcode.com/problems/first-missing-positive/ */
int firstMissingPositive(int* nums, int numsSize)
{
    if (NULL == nums || numsSize < 1)
        return 1;

    int i = 0;
    while (i < numsSize)
    {
        if (nums[i] != i + 1 && nums[i] > 0 && nums[i] < numsSize + 1 && nums[i] != nums[nums[i] - 1])
        {
            int nTmp = nums[nums[i] - 1];
            nums[nums[i] - 1] = nums[i];
            nums[i] = nTmp;
        }
        else
        {
            i++;
        }
    }

    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] != i + 1)
            return i + 1;
    }

    return i + 1;
}
