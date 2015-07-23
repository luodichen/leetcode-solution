/* https://leetcode.com/problems/triangle/ */
int minimumTotal(int **triangle, int numRows) 
{
    int size = sizeof(int) * numRows;
    int *best = (int *)malloc(size);
    int *tmp = (int *)malloc(size);
    
    int i = 0;
    int ret = 0;
    memset((void *)best, 0, size);
    memset((void *)tmp, 0, size);
    
    best[0] = triangle[0][0];
    
    for (i = 1; i < numRows; i++)
    {
        int j = 0;
        tmp[0] = triangle[i][0] + best[0];
        tmp[i] = triangle[i][i] + best[i - 1];
        for (j = 1; j < i; j++)
        {
            int choose = best[j] < best[j - 1] ? j : j - 1;
            tmp[j] = triangle[i][j] + best[choose];
        }
        
        memcpy((void *)best, (void *)tmp, size);
    }
    
    ret = best[0];
    for (i = 1; i < numRows; i++)
    {
        if (best[i] < ret)
            ret = best[i];
    }
    
    free((void *)best);
    free((void *)tmp);
    return ret;
}
