/* https://leetcode.com/problems/word-search-ii/ */

class TrieNode 
{
public:
    // Initialize your data structure here.
    TrieNode() 
        : m_bHasWord(false)
    {
        memset((void *)m_pSubs, 0, sizeof(m_pSubs));
    }
    
    ~TrieNode()
    {
        for (int i = 0; i < sizeof(m_pSubs) / sizeof(m_pSubs[0]); i++)
            if (NULL != m_pSubs[i])
            {
                delete m_pSubs[i];
                m_pSubs[i] = NULL;
            }
    }
    
    TrieNode *m_pSubs[26];
    bool m_bHasWord;
};

class Trie 
{
public:
    Trie() 
    {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) 
    {
        TrieNode *pCur = root;
        
        const char *szWord = word.c_str();
        char ch = '\0';
        while ((ch = *szWord) != '\0')
        {
            if (NULL == pCur->m_pSubs[ch - 'a'])
            {
                TrieNode *pNode = new TrieNode();
                pCur->m_pSubs[ch - 'a'] = pNode;
            }
            
            pCur = pCur->m_pSubs[ch - 'a'];
            szWord++;
        }

        pCur->m_bHasWord = true;
    }
    
    ~Trie()
    {
        delete root;
        root = NULL;
    }

    // Returns if the word is in the trie.
    bool search(string word) 
    {
        TrieNode *pNode = find(word);
        if (NULL == pNode)
            return false;
        else
            return pNode->m_bHasWord;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) 
    {
        return NULL != find(prefix);
    }
    
    TrieNode *find(std::string word, TrieNode *pFrom = NULL)
    {
        TrieNode *pRet = (NULL == pFrom) ? root : pFrom;
        const char *szWord = word.c_str();
        char ch = '\0';
        
        while ((ch = *szWord) != '\0')
        {
            if (NULL == pRet->m_pSubs[ch - 'a'])
                return NULL;
            else
                pRet = pRet->m_pSubs[ch - 'a'];
            
            szWord++;
        }
        
        return pRet;
    }

private:
    TrieNode* root;
};

class Solution
{
public:
    void search(std::vector<std::vector<char>> &board, 
            std::set<std::string> &result, std::string &stack,
            int nRow, int nCol, Trie &trie, TrieNode *pNode)
    {
        if ('\0' == board[nRow][nCol])
            return;

        int nRowSize = board.size();
        int nColSize = board[0].size();
        std::string strTarget;

        strTarget += board[nRow][nCol];

        stack += strTarget;
        board[nRow][nCol] = '\0';
        
        TrieNode *pNext = trie.find(strTarget, pNode);
        if (NULL == pNext)
        {
            board[nRow][nCol] = *stack.rbegin();
            stack.pop_back();
            return;
        }
        if (pNext->m_bHasWord)
            result.insert(std::string(stack));
        
        if (nRow + 1 < nRowSize)
            search(board, result, stack, nRow + 1, nCol, trie, pNext);
        if (nRow - 1 >= 0)
            search(board, result, stack, nRow - 1, nCol, trie, pNext);
        if (nCol + 1 < nColSize)
            search(board, result, stack, nRow, nCol + 1, trie, pNext);
        if (nCol - 1 >= 0)
            search(board, result, stack, nRow, nCol - 1, trie, pNext);
            
        board[nRow][nCol] = *stack.rbegin();
        stack.pop_back();
    }
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) 
    {
        int nRowSize = board.size();
        int nColSize = board[0].size();
        
        Trie trie;
        for (int i = 0; i < words.size(); i++)
            trie.insert(words[i]);
        
        std::set<std::string> result;
        std::string stack = "";
        for (int i = 0; i < nRowSize; i++)
            for (int j = 0; j < nColSize; j++)
                search(board, result, stack, i, j, trie, NULL);
        
        std::vector<std::string> ret;
        std::set<std::string>::iterator iter = result.begin();
        for (; iter != result.end(); iter++)
            ret.push_back(*iter);

        return ret;
    }
};
