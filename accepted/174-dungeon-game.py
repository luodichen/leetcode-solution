# https://leetcode.com/problems/dungeon-game/
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        dp = [0] * len(dungeon[0])
        for row in xrange(len(dungeon) - 1, -1, -1):
            for col in xrange(len(dungeon[0]) - 1, -1, -1):
                if col == len(dungeon[0]) - 1:
                    best = dp[col]
                elif row == len(dungeon) - 1:
                    best = dp[col + 1]
                else:
                    best = dp[col] if dp[col] < dp[col + 1] else dp[col + 1]
                    
                best -= dungeon[row][col]
                dp[col] = 0 if best < 0 else best
        
        return dp[0] + 1
