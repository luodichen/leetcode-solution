/* https://leetcode.com/problems/sort-colors/ */
void sortColors(int* nums, int numsSize)
{
    int counter[3] = {0};
    for (int i = 0; i < numsSize; i++)
        counter[nums[i]]++;

    for (int i = 0; i < sizeof(counter) / sizeof(counter[0]); i++)
        for (int j = 0; j < counter[i]; j++)
            *nums++ = i;
}

int main()
{
    int a[1] = {0};
    sortColors(a, 1);
    return 0;
}
