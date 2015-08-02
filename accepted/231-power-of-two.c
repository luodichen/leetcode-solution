/* https://leetcode.com/problems/power-of-two/ */
bool isPowerOfTwo(int n) 
{
    if (n < 1)
        return false;

    while (0 == (n & 1))
        n >>= 1;
    
    return 1 == n;
}
