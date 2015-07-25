/* https://leetcode.com/problems/product-of-array-except-self/ */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize)
{
    if (0 == numsSize)
        return nums;

    int *pLeft = (int *)malloc(sizeof(int) * numsSize);
    int *pRight = (int *)malloc(sizeof(int) * numsSize);

    pLeft[0] = nums[0];
    pRight[numsSize - 1] = nums[numsSize - 1];

    for (int i = 1; i < numsSize; i++)
    {
        pLeft[i] = pLeft[i - 1] * nums[i];
        pRight[numsSize - i - 1] = pRight[numsSize - i] * nums[numsSize - i - 1];
    }

    nums[0] = pRight[1];
    nums[numsSize - 1] = pLeft[numsSize - 2];

    for (int i = 1; i < numsSize - 1; i++)
    {
        nums[i] = pLeft[i - 1] * pRight[i + 1];
    }

    free((void *)pLeft);
    free((void *)pRight);

    *returnSize = numsSize;
    return nums;
}
