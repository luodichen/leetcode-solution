/* https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ */
#define SAME_FLAG(a, b) (((a) > 0 && (b) > 0) || ((a) < 0 && (b) < 0))
#define FLAG_CORRECT(n, r, f) ((((n) > (r)) && ((f) > 0)) || (((n) < (r)) && ((f) < 0)))
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MIN3(a, b, c) (MIN(a, MIN(b, c)))

int findMin(int* nums, int numsSize)
{
    if (1 == numsSize) return nums[0];
    else if (2 == numsSize) return MIN(nums[0], nums[1]);
    else if (3 == numsSize) return MIN3(nums[0], nums[1], nums[2]);

    int left = 0;
    int right = numsSize - 1;

    if (!SAME_FLAG(nums[right] - nums[left], nums[left] - nums[left + 1]))
        return MIN3(nums[right], nums[left], nums[left + 1]);
    if (!SAME_FLAG(nums[right - 1] - nums[right], nums[right] - nums[left]))
        return MIN3(nums[right - 1], nums[right], nums[left]);

    int flag = (nums[1] > nums[0]) ? 1 : -1;
    int nLeftRef = nums[0];
    int nRightRef = nums[numsSize - 1];

    while (right - left > 1)
    {
        int nNext = (left + right) / 2;
        if (FLAG_CORRECT(nums[nNext], nLeftRef, flag))
            left = nNext;
        else if (FLAG_CORRECT(nRightRef, nums[nNext], flag))
            right = nNext;
        else
            return -9999; /* that's impossible */
    }

    return MIN(nums[left], nums[right]);
}
