# https://leetcode.com/problems/bulls-and-cows/

class Solution(object):
    def getHint(self, secret, guess):
        bulls, cows = 0, 0
        map = [0] * 10
        
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                map[int(secret[i])] += 1
            
        for i in xrange(len(secret)):
            if secret[i] != guess[i] and map[int(guess[i])] > 0:
                map[int(guess[i])] -= 1
                cows += 1
        
        return '%dA%dB' % (bulls, cows, )
