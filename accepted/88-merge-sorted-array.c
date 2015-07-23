/* https://leetcode.com/problems/merge-sorted-array/ */
void merge(int* nums1, int m, int* nums2, int n) 
{
    int nRetSize = sizeof(int) * (m + n);
    int *pTmp = (int *)malloc(nRetSize);
    int i = 0;
    memset((void *)pTmp, 0, nRetSize);
    
    int flag = 0;
    for (i = 0; i < m - 1; i++)
    {
        if (nums1[i] != nums1[i + 1])
        {
            flag = nums1[i + 1] - nums1[i];
            break;
        }
    }
    
    for (i = 0; (i < n - 1) && (flag != 0); i++)
    {
        if (nums2[i] != nums2[i + 1])
        {
            flag = nums2[i + 1] - nums2[i];
            break;
        }
    }
    
    flag = (0 == flag) ? 1 : flag;
    
    int *p = nums1, *q = nums2;
    for (i = 0; i < m + n; i++)
    {
        if ((p - nums1 >= m) || (q - nums2 >= n))
            pTmp[i] = (p - nums1 >= m) ? *q++ : *p++;
        else
            pTmp[i] = (flag > 0 && *p > *q) ? *q++ : *p++;
    }
    
    memcpy((void *)nums1, (void *)pTmp, nRetSize);
    free((void *)pTmp);
}
