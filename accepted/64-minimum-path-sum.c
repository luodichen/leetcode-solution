/* https://leetcode.com/problems/minimum-path-sum/ */
#define D(d, cs, r, c) (*((d) + (cs) * (r) + (c)))
#define DP(r, c) (D(dp, gridColSize, r, c))
int minPathSum(int** grid, int gridRowSize, int gridColSize) {
    int *dp = (int *)malloc(sizeof(int) * gridRowSize * gridColSize);
    for (int row = 0; row < gridRowSize; row++)
        for (int col = 0; col < gridColSize; col++)
            if (0 == row && 0 == col)
                DP(row, col) = grid[0][0];
            else
                DP(row, col) = (((0 == row) || (DP(row, col - 1) < DP(row - 1, col))) ?
                        DP(row, col - 1) : DP(row - 1, col)) + grid[row][col];
    int ret = DP(gridRowSize - 1, gridColSize - 1);
    free((void *)dp);
    return ret;
}
