/* https://leetcode.com/problems/bulls-and-cows/ */

char* getHint(char* secret, char* guess) 
{
    int nBulls = 0;
    int nCows = 0;
    
    int map[10] = { 0 };
    
    for (int i = 0; secret[i] != '\0'; i++)
        if (secret[i] == guess[i])
            nBulls++;
        else
            map[secret[i] - '0']++;
    
    for (int i = 0; secret[i] != '\0'; i++)
        secret[i] != guess[i] && map[guess[i] - '0']-- > 0 && nCows++;
    
    static char ret[32] = {0};
    sprintf(ret, "%dA%dB", nBulls, nCows);
    
    return ret;
}
