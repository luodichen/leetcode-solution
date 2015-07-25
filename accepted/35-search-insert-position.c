/* https://leetcode.com/problems/search-insert-position/ */
int searchInsert(int* nums, int numsSize, int target) {
    if (target <= nums[0])
        return 0;
    if (target > nums[numsSize - 1])
        return numsSize;

    int nLeftEdge = 0;
    int nRightEdge = numsSize - 1;

    while (nRightEdge - nLeftEdge > 1)
    {
        int nTest = (nRightEdge + nLeftEdge) / 2;
        if (target == nums[nTest])
            return nTest;
        else if (target < nums[nTest])
            nRightEdge = nTest;
        else
            nLeftEdge = nTest;
    }

    return nRightEdge;
}

