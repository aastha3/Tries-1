# Model solution : https://leetcode.com/problems/longest-word-in-dictionary/discuss/203730/Python-Trie-%2B-DFS-(No-extensive-loops-or-complicated-TrieNode)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # build a Trie 
        # each char is true and length = maxLength so far     
        class TrieNode:
            def __init__(self):
                self.children ={}
                self.end = False
        
        class Trie:
            def __init__(self):
                self.root =TrieNode()
                
            def insert(self, word):
                curr = self.root
                
                for c in word: 
                    if c not in curr.children:
                        curr.children[c] = TrieNode()
                    curr = curr.children[c]
                curr.end = True
                              
            def longest_word(self):
                def helper(node, partial_res):
                    res = partial_res 
                    
                    for c , child in node.children.items():
                        if child.end:
                            pot = helper(child, partial_res+c)
                            if len(pot) > len(res):
                                res = pot 
                            elif len(pot) == len(res) and pot < res:
                                res =pot 
                    return res 
                return helper(self.root, "")
                            
        T = Trie()
        for word in words:
            T.insert(word)
        return T.longest_word()
