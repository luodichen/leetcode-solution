/* https://leetcode.com/problems/search-a-2d-matrix/ */
bool searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) 
{
    if (NULL == matrix || matrixRowSize <= 0 || matrixColSize <= 0)
        return false;
    
    int nRowSize = matrixRowSize, nColSize = matrixColSize;
    if (target < matrix[0][0] || target > matrix[nRowSize - 1][nColSize - 1])
        return false;
    
    int nTop = 0, nBottom = nRowSize - 1;
    
    if (target == matrix[nRowSize - 1][0])
        return true;
    else if (target >= matrix[nRowSize - 1][0])
        nTop = nBottom;
    
    while (nBottom - nTop > 1)
    {
        int nTmp = (nBottom + nTop) / 2;
        if (matrix[nTmp][0] == target)
            return true;
        else if (matrix[nTmp][0] < target)
            nTop = nTmp;
        else
            nBottom = nTmp;
    }
    
    int nLeft = 0;
    int nRight = nColSize - 1;
    
    if (target == matrix[nTop][nRight])
        return true;
    
    while (nRight - nLeft > 1)
    {
        int nTmp = (nLeft + nRight) / 2;
        if (matrix[nTop][nTmp] == target)
            return true;
        else if (matrix[nTop][nTmp] < target)
            nLeft = nTmp;
        else
            nRight = nTmp;
    }
    
    return matrix[nTop][nLeft] == target || matrix[nTop][nRight] == target;
}
