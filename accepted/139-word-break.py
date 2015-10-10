# https://leetcode.com/problems/word-break/
class TrieNode(object):
    def __init__(self):
        self.map = {}
        self.marked = False

class Solution(object):
    def wordBreak(self, s, wordDict):
        trie_root = TrieNode()
        
        for word in wordDict:
            cur = trie_root
            for c in word:
                if c not in cur.map:
                    cur.map[c] = TrieNode()
                cur = cur.map[c]
            cur.marked = True
        
        tails = set([trie_root, ])
        for c in s:
            if len(tails) == 0:
                return False
            new_tails = set()
            for tail in tails:
                if c in tail.map:
                    cur = tail.map[c]
                    new_tails.add(cur)
                    if cur.marked:
                        new_tails.add(trie_root)
            tails = new_tails
        
        for tail in tails:
            if tail.marked:
                return True
        return False
