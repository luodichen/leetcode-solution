/* https://leetcode.com/problems/surrounded-regions/ */
class Solution 
{
public:
    void saver(std::vector<std::vector<char>>& board, int nRowSize, int nColSize, int nRow, int nCol)
    {
        if ('O' != board[nRow][nCol])
            return;

        std::queue<std::pair<int, int>> q;
        std::pair<int, int> node(nRow, nCol);
        q.push(node);

        while (!q.empty())
        {
            std::pair<int, int> node = q.front();
            q.pop();
            nRow = node.first;
            nCol = node.second;
            if ('O' != board[nRow][nCol])
                continue;
            board[nRow][nCol] = 'S';

            if (nRow - 1 >= 0 && 'O' == board[nRow - 1][nCol])
            {
                std::pair<int, int> node(nRow - 1, nCol);
                q.push(node);
            }
            if (nRow + 1 <= nRowSize - 1 && 'O' == board[nRow + 1][nCol])
            {
                std::pair<int, int> node(nRow + 1, nCol);
                q.push(node);
            }
            if (nCol - 1 >= 0 && 'O' == board[nRow][nCol - 1])
            {
                std::pair<int, int> node(nRow, nCol - 1);
                q.push(node);
            }
            if (nCol + 1 <= nColSize - 1 && 'O' == board[nRow][nCol + 1])
            {
                std::pair<int, int> node(nRow, nCol + 1);
                q.push(node);
            }
        }
    }

    void solve(std::vector<std::vector<char>>& board) 
    {
        if (board.empty())
            return;

        int nRowSize = board.size();
        int nColSize = board[0].size();

        for (int nRow = 0; nRow < nRowSize; nRow++)
        {
            if (0 == nRow || ((nRowSize - 1) == nRow))
            {
                for (int nCol = 0; nCol < nColSize; nCol++)
                    saver(board, nRowSize, nColSize, nRow, nCol);
            }
            else
            {
                saver(board, nRowSize, nColSize, nRow, 0);
                saver(board, nRowSize, nColSize, nRow, nColSize - 1);
            }
        }

        for (int nRow = 0; nRow < nRowSize; nRow++)
            for (int nCol = 0; nCol < nColSize; nCol++)
                if ('S' == board[nRow][nCol])
                    board[nRow][nCol] = 'O';
                else if ('O' == board[nRow][nCol])
                    board[nRow][nCol] = 'X';
    }
};
