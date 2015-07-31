/* https://leetcode.com/problems/implement-trie-prefix-tree/ */
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
    
private:
    TrieNode *find(std::string word)
    {
        TrieNode *pRet = root;
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

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");
