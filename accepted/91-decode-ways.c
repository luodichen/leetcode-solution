/* https://leetcode.com/problems/decode-ways/ */
int numDecodings(char* s) 
{
    if (*s < '1' || *s > '9')
        return 0;
    
    int nAcc[2] = {1, 0};
    char cPrev = *s++;
    
    while ('\0' != *s)
    {
        if (*s < '0' || *s > '9' || ('0' == *s && '0' == cPrev))
            return 0;
        
        int nSingle = *s > '0' ? (nAcc[0] + nAcc[1]) : 0;
        int nPair = 0;
        if (((cPrev - '0') * 10 + *s - '0' <= 26) && cPrev > '0')
            nPair = nAcc[0];
        
        nAcc[0] = nSingle;
        nAcc[1] = nPair;
        
        cPrev = *s++;
    }
    
    return nAcc[0] + nAcc[1];
}
