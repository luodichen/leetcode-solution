/* https://leetcode.com/problems/number-of-islands/ */
void distory_island(char **grid, int nRowSize, int nColSize, int nRow, int nCol)
{
    if ('0' == grid[nRow][nCol])
        return;
    
    grid[nRow][nCol] = '0';
    
    if (nRow - 1 >= 0)
        distory_island(grid, nRowSize, nColSize, nRow - 1, nCol);
    if (nRow + 1 <= nRowSize - 1)
        distory_island(grid, nRowSize, nColSize, nRow + 1, nCol);
    if (nCol - 1 >= 0)
        distory_island(grid, nRowSize, nColSize, nRow, nCol - 1);
    if (nCol + 1 <= nColSize - 1)
        distory_island(grid, nRowSize, nColSize, nRow, nCol + 1);
}

int numIslands(char** grid, int gridRowSize, int gridColSize) 
{
    int nRet = 0;
    for (int nRow = 0; nRow < gridRowSize; nRow++)
    {
        for (int nCol = 0; nCol < gridColSize; nCol++)
        {
            if ('1' == grid[nRow][nCol])
            {
                nRet++;
                distory_island(grid, gridRowSize, gridColSize, nRow, nCol);
            }
        }
    }
    
    return nRet;
}
