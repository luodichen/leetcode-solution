# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        result = 0
        queue = []
        char_set = set()
        
        for c in s:
            if c not in char_set:
                char_set.add(c)
                queue.append(c)
                
                result = len(queue) if len(queue) > result else result
            else:
                while queue[0] != c:
                    char_set.remove(queue.pop(0))
                queue.append(queue.pop(0))
        
        return result
