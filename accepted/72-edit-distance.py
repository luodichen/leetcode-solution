# https://leetcode.com/problems/edit-distance/
class Solution(object):
    def minDistance(self, word1, word2):
        dp = range(len(word1) + 1)
        col_index = 0
        for c in word2:
            col_index += 1
            prev = dp[0]
            for i in xrange(1, len(word1) + 1):
                add = dp[i] + 1
                rm = dp[i - 1] + 1
                rp = prev if c == word1[i - 1] else prev + 1
                
                prev = dp[i]
                t = add if add < rm else rm
                t = t if t < rp else rp
                dp[i] = t
                
            dp[0] = col_index
        return dp[len(word1)]
