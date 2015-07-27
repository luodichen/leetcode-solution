/* https://leetcode.com/problems/unique-binary-search-trees/ */
int uniquePaths(int m, int n) {
    int dp[100] = {1, 0};
    
    for (int i = 0; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[j] += dp[j - 1];
    return dp[n - 1];
}
