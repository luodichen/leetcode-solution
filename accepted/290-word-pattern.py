# https://leetcode.com/problems/word-pattern/
class Solution(object):
    def wordPattern(self, pattern, str):
        words_set = set()
        table = {}
        words = str.split(' ')
        
        if len(pattern) != len(words):
            return False
        
        for i in xrange(len(pattern)):
            if pattern[i] not in table:
                if words[i] in words_set:
                    return False
                table[pattern[i]] = words[i]
                words_set.add(words[i])
            elif table[pattern[i]] != words[i]:
                return False
        
        return True
