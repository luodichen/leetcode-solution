/* https://leetcode.com/problems/word-search/ */
bool search(char **board, int nRowSize, int nColSize, int nRow, int nCol, char *szWord)
{
    if (*szWord != board[nRow][nCol])
        return false;
    else if ('\0' == *(szWord + 1))
        return true;
    
    char cTmp = board[nRow][nCol];
    board[nRow][nCol] = '\0';

    if ((nCol + 1 < nColSize) 
            && search(board, nRowSize, nColSize, nRow, nCol + 1, szWord + 1))
        return true;
    else if ((nCol - 1 >= 0)
            && search(board, nRowSize, nColSize, nRow, nCol - 1, szWord + 1))
        return true;
    else if ((nRow + 1 < nRowSize)
            && search(board, nRowSize, nColSize, nRow + 1, nCol, szWord + 1))
        return true;
    else if ((nRow - 1 >= 0)
            && search(board, nRowSize, nColSize, nRow - 1, nCol, szWord + 1))
        return true;
    
    board[nRow][nCol] = cTmp;
    return false;
}

bool exist(char** board, int boardRowSize, int boardColSize, char* word) 
{
    for (int i = 0; i < boardRowSize; i++)
        for (int j = 0; j < boardColSize; j++)
            if (search(board, boardRowSize, boardColSize, i, j, word))
                return true;
    
    return false;
}
