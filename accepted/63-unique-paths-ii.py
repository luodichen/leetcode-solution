class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0:
            return 0
        
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1 if 0 == obstacleGrid[0][0] else 0
        for row in obstacleGrid:
            dp[0] = 1 if 0 == row[0] and 1 == dp[0] else 0
            for i in xrange(1, len(row)):
                dp[i] = dp[i] + dp[i - 1] if 0 == row[i] else 0
        
        return dp[len(obstacleGrid[0]) - 1]
