/* https://leetcode.com/problems/count-primes/ */
class Solution 
{
public:
    int countPrimes(int n) 
    {
        char *pTable = new char[n];
        memset((void *)pTable, 1, n);
        int ret = 0;
        
        int i = 2;
        for (; i * i < n; i++)
        {
            if (pTable[i])
            {
                ret++;
                int num = i;
                while (i + num < n)
                    pTable[num = i + num] = 0;
            }
        }
        
        for (; i < n; i++)
            if (pTable[i])
                ret++;
        
        return ret;
    }
};
