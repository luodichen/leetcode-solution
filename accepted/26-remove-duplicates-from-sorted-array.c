/* https://leetcode.com/problems/remove-duplicates-from-sorted-array/ */
int removeDuplicates(int* nums, int numsSize)
{
    if (numsSize < 1 || NULL == nums)
        return 0;

    int write = 1;
    int prev = nums[0];

    for (int i = 1; i < numsSize; i++)
        if (nums[i] != prev)
            prev = nums[write++] = nums[i];
    return write;
}
