/* https://leetcode.com/problems/ugly-number/ */
bool isUgly(int num) 
{
    int nPrimes[] = {2, 3, 5};
    if (num < 1)
        return false;
    
    for (int i = 0; i < (sizeof(nPrimes) / sizeof(nPrimes[0])); i++)
        while ((num > 0) && (num % nPrimes[i] == 0))
            num /= nPrimes[i];
    
    return 1 == num;
}
