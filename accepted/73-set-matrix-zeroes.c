/* https://leetcode.com/problems/set-matrix-zeroes/ */
void setZeroes(int** matrix, int matrixRowSize, int matrixColSize)
{
    int zero_on_row = 0;
    int zero_on_col = 0;
    
    for (int i = 0; i < matrixColSize; i++)
    {
        if (0 == matrix[0][i])
        {
            zero_on_row = 1;
            break;
        }
    }
    
    for (int i = 0; i < matrixRowSize; i++)
    {
        if (0 == matrix[i][0])
        {
            zero_on_col = 1;
            break;
        }
    }
    
    for (int i = 1; i < matrixRowSize; i++)
    {
        for (int j = 1; j < matrixColSize; j++)
            if (0 == matrix[i][j])
                matrix[0][j] = 0, matrix[i][0] = 0;
    }
    
    for (int i = 1; i < matrixColSize; i++)
        if (0 == matrix[0][i])
            for (int j = 1; j < matrixRowSize; j++)
                matrix[j][i] = 0;
    
    for (int i = 1; i < matrixRowSize; i++)
        if (0 == matrix[i][0])
            for (int j = 1; j < matrixColSize; j++)
                matrix[i][j] = 0;
    
    if (zero_on_row)
        for (int i = 0; i < matrixColSize; i++)
            matrix[0][i] = 0;
    
    if (zero_on_col)
        for (int i = 0; i < matrixRowSize; i++)
            matrix[i][0] = 0;
}
