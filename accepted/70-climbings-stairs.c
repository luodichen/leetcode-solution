/* https://leetcode.com/problems/climbing-stairs/ */
int climbStairs(int n)
{
    if (1 == n)
        return 1;
    
    int dp[] = {1, 2};
    for (int i = 0; i < n - 2; i++)
    {
        int tmp = dp[1];
        dp[1] += dp[0];
        dp[0] = tmp;
    }
    
    return dp[1];
}
